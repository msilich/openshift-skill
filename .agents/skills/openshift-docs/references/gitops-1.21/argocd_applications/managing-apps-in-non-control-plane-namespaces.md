<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

As a cluster administrator, you can create and manage the `Application` resources in non-control plane namespaces declaratively other than the `openshift-gitops` control plane namespace. This functionality is called the *Applications in any namespace* feature in the Argo CD open source project.

> [!NOTE]
> As a developer, if you are creating Argo CD applications in non-control plane namespaces other than the `openshift-gitops` control plane namespace, ensure that your cluster administrator grants the necessary permissions to them.

Otherwise, after the Argo CD reconciliation, you will see an error message similar to the following example:

**Example error message:**

``` terminal
error while validating and normalizing app: error getting application's project: application 'app' in namespace 'dev' is not allowed to use project 'default'
```

To use this functionality, you must explicitly enable and configure the target namespaces in the following objects:

- The `ArgoCD` custom resource (CR) of your user-defined cluster-scoped Argo CD instance

- The `AppProject` custom resource (CR)

- The `Application` CR

The process of creating and managing the `Application` resources in non-control plane namespaces consists of the following procedures:

1.  [Configuring the `ArgoCD` CR of your user-defined cluster-scoped Argo CD instance with the target namespaces](managing-apps-in-non-control-plane-namespaces.md#gitops-configuring-argo-cd-cr-of-your-user-defined-cluster-scoped-instance-with-target-namespaces_managing-apps-in-non-control-plane-namespaces).

2.  [Creating and configuring a user-defined `AppProject` instance in the `openshift-gitops` control plane namespace and specify the target namespaces in the `.spec.sourceNamespaces` field of the user-defined `AppProject` instance](managing-apps-in-non-control-plane-namespaces.md#gitops-creating-and-configuring-user-defined-appproject-instance-with-target-namespaces_managing-apps-in-non-control-plane-namespaces).

3.  [Configuring the `metadata.namespace` and `.spec.project` fields of the `Application` CR to reference the target namespaces and user-defined `AppProject` instance](managing-apps-in-non-control-plane-namespaces.md#gitops-creating-and-configuring-the-app-cr-to-reference-the-target-namespace-and-user-defined-appproject-instance_managing-apps-in-non-control-plane-namespaces).

This functionality is useful in multitenancy environments when you want to manage deployments of Argo CD applications for your isolated teams.

> [!IMPORTANT]
> To prevent privilege escalations for your application teams, you must meet the following requirements:
>
> - Do not configure non-control plane namespaces in the `.spec.sourceNamespaces` field of any privileged `AppProject` instance, for example, the `default` instance of your `AppProject` CR installed in either the `openshift-gitops` control plane namespace or your defined namespace.
>
> - Do not grant access to the `openshift-gitops` control plane namespace within the `AppProject` CRD.
>
> - Always create and configure user-defined `AppProject` instances in the `openshift-gitops` control plane namespace, and then configure non-control plane namespaces in the `.spec.sourceNamespaces` field within the corresponding user-defined `AppProject` instance.

# Prerequisites

- You have installed Red Hat OpenShift GitOps 1.13.0 or a later version on your OpenShift Container Platform cluster.

- You have a user-defined [cluster-scoped Argo CD instance](../declarative_clusterconfig/configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.md#using-argo-cd-instance-to-manage-cluster-scoped-resources_configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations) in your defined namespace, for example, `spring-petclinic` namespace.

# Configuring the Argo CD CR of your user-defined cluster-scoped Argo CD instance with the target namespaces

As a cluster administrator, you can define a certain set of non-control plane namespaces in which users can create, update, and reconcile `Application` resources. You must first explicitly configure the target namespaces in the `ArgoCD` custom resource (CR) of your user-defined cluster-scoped Argo CD instance per your requirements.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the OpenShift Container Platform cluster as an administrator.

- You have installed Red Hat OpenShift GitOps 1.13.0 or a later version on your OpenShift Container Platform cluster.

- You have a user-defined cluster-scoped Argo CD instance in your defined namespace, for example, `spring-petclinic` namespace.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the **Administrator** perspective of the web console, click **Operators** → **Installed Operators**.

2.  From the **Project** list, select the project where the user-defined cluster-scoped Argo CD instance is installed.

3.  Select **Red Hat OpenShift GitOps** from the installed Operators list and go to the **Argo CD** tab.

4.  Click your user-defined cluster-scoped Argo CD instance.

5.  Configure the `ArgoCD` CR of your user-defined cluster-scoped Argo CD instance with the target namespaces:

    1.  Click the **YAML** tab and edit the YAML file of the `ArgoCD` CR.

    2.  In the `ArgoCD` CR, set the value of the `sourceNamespaces` parameter to include the non-control plane namespaces:

        **Example `ArgoCD` CR:**

        ``` yaml
        apiVersion: argoproj.io/v1beta1
        kind: ArgoCD
        metadata:
          name: example
          namespace: spring-petclinic
        spec:
          sourceNamespaces:
            - dev
            - app-team-*
        ```

        where:

        `metadata.name`
        Specifies the name of the user-defined cluster-scoped Argo CD instance.

        `metadata.namespace`
        Specifies the namespace where the user-defined cluster-scoped Argo CD instance is created.

        `spec.sourceNamespaces`
        Specifies the namespaces where users can create and manage `Application` resources handled by the Argo CD instance. You can use wildcard patterns (`*`), to allow the Argo CD instance to manage `Application` resources in matching namespaces like `app-team-1` or `app-team-2`.

    3.  Click **Save** and **Reload**.

        > [!NOTE]
        > When a target namespace is specified under the `sourceNamespaces` field, the Operator adds the `argocd.argoproj.io/managed-by-cluster-argocd` label to the specified namespace.

        **Example `dev` target namespace:**

        ``` yaml
        apiVersion: v1
        kind: Namespace
        metadata:
          name: dev
          labels:
            argocd.argoproj.io/managed-by-cluster-argocd: spring-petclinic
            kubernetes.io/metadata.name: dev
        ```

        where:

        `metadata.name`
        Specifies the name of the namespace.

        `argocd.argoproj.io/managed-by-cluster-argocd`
        Specifies the Argo CD instance (`spring-petclinic`) that owns and manages this namespace.

6.  Verify that Operator adds the `argocd.argoproj.io/managed-by-cluster-argocd` label to the specified namespace:

    1.  Go to **Administration** → **Namespaces** and click **Create Namespace**.

    2.  In the **Create Namespace** dialog box, provide the **Name** and click **Create**.

        For example, to create `dev` target namespace, enter `dev` in the **Name** field. You can repeat the previous steps to create the `app-team-1` and `app-team-2` target namespaces.

        The **Namespaces** page displays the created target namespaces.

    3.  Click the target namespace and go to the **YAML** tab to verify the `argocd.argoproj.io/managed-by-cluster-argocd` label added by the Operator.

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

When you create a cluster-scoped Argo CD instance, the GitOps Operator automatically creates the required RBAC resources. Verify that these resources exist to ensure that the Argo CD instance can manage cluster-scoped and namespace-scoped resources.

</div>

1.  Verify that your user-defined cluster-scoped Argo CD instance is configured with a cluster role to manage cluster-scoped resources:

    1.  Go to **User Management** → **Roles** and from the **Filter** list, select **Cluster-wide Roles**.

    2.  Search for the created cluster roles by using the **Search by name** field. For example, `example-spring-petclinic-argocd-application-controller` and `example-spring-petclinic-argocd-server`.

        The **Roles** page displays the created cluster roles.

    3.  Verify that the following role-based access control (RBAC) resources are created by the GitOps Operator:

        | Name | Kind | Purpose |
        |----|----|----|
        | `<argocd_name>-<argocd_namespace>-argocd-application-controller` | `ClusterRole` and `ClusterRoleBinding` | For the Argo CD Application Controller to watch and list `Application` resources at cluster-level |
        | `<argocd_name>-<argocd_namespace>-argocd-server` | `ClusterRole` and `ClusterRoleBinding` | For the Argo CD Server to watch and list `Application` resources at cluster-level |
        | `<argocd_name>-<target_namespace>` | `Role` and `RoleBinding` | For the Argo CD server to manage `Application` resources in target namespace through the UI, API, or CLI |

# Additional resources

- [Installing a user-defined Argo CD instance](../argocd_instance/setting-up-argocd-instance.md#setting-up-argocd-instance)

# Creating and configuring a user-defined AppProject instance with the target namespaces

As a cluster administrator, you can define a certain set of non-control plane namespaces in which users can create, update, and reconcile `Application` resources. After you configure your user-defined cluster-scoped Argo CD instance with target namespaces, you must create and configure a user-defined `AppProject` instance in the `openshift-gitops` control plane namespace. In addition, you must explicitly configure the target namespaces in the `.spec.sourceNamespaces` field of the user-defined `AppProject` instance.

> [!NOTE]
> Applications in the GitOps control plane namespace (`openshift-gitops`) are allowed to set their `.spec.project` field to reference any `AppProject` instance, regardless of the restrictions placed by the `.spec.sourceNamespaces` field in the `AppProject` custom resource (CR).

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the OpenShift Container Platform cluster as an administrator.

- You have installed Red Hat OpenShift GitOps 1.13.0 or a later version on your OpenShift Container Platform cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create and configure a user-defined `AppProject` instance in the `openshift-gitops` control plane namespace to specify the target namespaces in the `.spec.sourceNamespaces` field:

    1.  From the **Project** list, select the `openshift-gitops` project.

    2.  In the **Administrator** perspective of the web console, click **Operators** → **Installed Operators** → **Red Hat OpenShift GitOps** and go to the **AppProject** tab.

    3.  Click **Create AppProject** and enter the following configuration in the YAML view:

        **Example user-defined `AppProject` instance:**

        ``` yaml
        kind: AppProject
        apiVersion: argoproj.io/v1alpha1
        metadata:
          name: project-one
          namespace: openshift-gitops
        spec:
          sourceNamespaces:
            - dev
            - app-team-*
          destinations:
            - name: '*'
              namespace: '*'
              server: '*'
          sourceRepos:
            - '*'
        ```

        where:

        `metadata.name`
        Specifies the name of the user-defined `AppProject` instance.

        `metadata.namespace`
        Specifies the control plane namespace where you want to run the user-defined `AppProject` instance.

        `spec.sourceNamespaces`
        Specifies the list of non-control plane namespaces for creating and managing `Application` resources.

        `spec.destinations`
        Specifies the clusters and namespaces where applications within this `AppProject` can deploy resources. Using wildcard values allows deployments to any cluster, server, or namespace.

        `spec.sourceRepos`
        Specifies the Git repositories from which applications within this `AppProject` can pull manifests. Using a wildcard allows any repository.

    4.  Click **Create**.

        The **AppProjects** page displays the created user-defined `AppProject` instance.

</div>

# Creating and configuring the Application CR to reference the target namespace and user-defined AppProject instance

As a cluster administrator, you can define a certain set of non-control plane namespaces in which users can create, update, and reconcile `Application` resources. After you configure the target namespaces in the `.spec.sourceNamespaces` field of the user-defined `AppProject` instance, you must explicitly create and configure the `Application` custom resource (CR) with the parameters for the `metadata.namespace` and `.spec.project` fields to reference the target namespace and user-defined `AppProject` instance.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the OpenShift Container Platform cluster as an administrator.

- You have installed Red Hat OpenShift GitOps 1.13.0 or a later version on your OpenShift Container Platform cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create and configure the `Application` CR with the parameters for the `metadata.namespace` and `.spec.project` fields to reference the target namespace and user-defined `AppProject` instance:

    1.  From the **Project** list, select the target namespace.

    2.  In the **Administrator** perspective of the web console, click **Operators** → **Installed Operators** → **Red Hat OpenShift GitOps** and go to the **Application** tab.

    3.  Click **Create Application** and enter the following configuration in the YAML view:

        **Example Application CR:**

        ``` yaml
        kind: Application
        apiVersion: argoproj.io/v1alpha1
        metadata:
          name: cluster-configs
          namespace: dev
        spec:
          project: project-one
          # ...
        ```

        where:

        `metadata.name`
        Specifies the name of the application.

        `metadata.namespace`
        Specifies the target namespace where the Application CR is created.

        `spec.project`
        Specifies the name of the AppProject that this application belongs to.

    4.  Click **Create**.

        The **Applications** page displays the created application.

    The `cluster-configs` Argo CD application now has the statuses **Healthy** and **Synced**.

</div>

# Additional resources

- [Creating an application by using the Argo CD dashboard](../declarative_clusterconfig/configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.md#creating-an-application-by-using-the-argo-cd-dashboard_configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations)

- [Managing the application set resources in non-control plane namespaces](../argocd_application_sets/managing-app-sets-in-non-control-plane-namespaces.md#managing-app-sets-in-non-control-plane-namespaces)
