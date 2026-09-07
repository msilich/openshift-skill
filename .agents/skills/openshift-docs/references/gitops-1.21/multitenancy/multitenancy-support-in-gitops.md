<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Multitenancy is a software architecture where a single software instance serves many distinct user groups, or tenants. Using multitenancy, you can share a single Argo CD instance to deploy resources while maintaining isolation between users. Understanding Argo CD instance scopes helps you choose the appropriate mode for your environment.

With Red Hat OpenShift GitOps Operator on OpenShift Container Platform, as a cluster administrator, you can give multitenant access to the cluster for application delivery teams (tenants). You can allow tenants to create and manage dedicated Argo CD instances in their user-defined namespaces without having administrative permissions. The tenants have full autonomy and can tailor this instance to their needs and requirements without interfering with other tenants.

> [!NOTE]
> For a multitenant cluster, the person managing the Argo CD instance might not be the person who manages the cluster and its users. Therefore, you cannot have the Argo CD Application Controller (`argocd-application-controller` component) as a superuser in the cluster.

The Argo CD Application Controller reconciles resources in managed clusters. To use multitenancy in the GitOps Operator, configure permissions based on your use cases and tenant requirements. Explicitly grant, extend, or restrict permissions for Argo CD instances, applications, and remote clusters to control operations.

# Argo CD instance scopes

The Red Hat OpenShift GitOps Operator creates instances that you can classify broadly into the following modes, all supporting multitenancy:

- Namespace-scoped instance (Application delivery instance)

- Cluster-scoped instance

- Default cluster-scoped instance

## Namespace-scoped instance (Application delivery instance)

After you create an Argo CD custom resource (CR) in one of your namespaces, the GitOps Operator starts an Argo CD in this namespace, which you can use for application delivery. In its initial state, this instance has permission to deploy resources only in the same namespace in which it is installed. However, you might need to configure the instance to meet your specific requirements.

With the GitOps Operator, you can extend the permissions of the Argo CD instance to enable the Argo CD Application Controller to deploy resources into other namespaces apart from where it is installed.

> [!NOTE]
> The roles that the GitOps Operator in the namespace creates are namespace-scoped and only have access to namespace resources. The Operator cannot perform any actions outside of the namespaces it manages.

**How does this method work?**

The GitOps Operator allows OpenShift users to instantiate Argo CD instances in their namespaces, provided that they have permission to create Argo CD resources in the `argoproj.io/v1alpha1` or `argoproj.io/v1beta1` API in their namespace. Currently, a namespace-scoped instance has full administrative permissions for one or many namespaces it manages, similar to allowing all verbs for all resources within that namespace.

For the Argo CD Application Controller to deploy resources in other namespaces, you must configure Kubernetes roles and role bindings. These roles and bindings identify the namespaces that a namespace-scoped instance can manage. The GitOps Operator supports the argocd.argoproj.io/managed-by label to simplify this setup. Use this label to indicate the namespaces managed by the instance. When you deploy the GitOps Operator in namespace-scoped mode, it automatically creates the required roles and role bindings in each labeled namespace.

> [!IMPORTANT]
> The `argocd.argoproj.io/managed-by` label only works for namespaces in the same cluster as the GitOps Operator. For remote clusters, you must define the permissions manually.

By default, when labeling the namespace by using the `managed-by` label, the GitOps Operator gives the Argo CD Application Controller permissions equal to the Kubernetes default `admin` cluster role for the labeled namespace. However, you can opt to define an alternate cluster role that is used for the controller and server components by using the `CONTROLLER_CLUSTER_ROLE` and `CONTROLLER_SERVER_ROLE` environment variables in the Operator’s `Subscription` resource. When you give these variables, the Operator will not create a default role in the namespace but rather only create a role binding in the namespace of the corresponding cluster role. It is up to the administrator to create the cluster role, having full control over the permissions.

<div class="note">

<div class="title">

</div>

- When defining your role, Argo CD will attempt to interact with all resources. Therefore, you must either give permission to `view`, `get`, and `watch` all resources in your custom cluster role, or configure the Argo CD CR to include or exclude specific resources through the `resourceInclusions` or `resourceExclusions` fields defined in the role.

- It is not possible to manage cluster-scoped resources, such as namespaces, custom resource definitions (CRDs), or cluster roles with a namespace-scoped instance.

</div>

# Additional resources

- [Deploying resources to a different namespace](../argocd_instance/setting-up-argocd-instance.md#gitops-deploy-resources-different-namespaces_setting-up-argocd-instance)

## Cluster-scoped instance

A cluster-scoped instance is intended to deploy and manage resources across a cluster.

> [!NOTE]
> If you intend to use the *Applications in any namespace* feature, choose the mode of the Argo CD instance scope as cluster-scoped instance.

Cluster-scoped instances have access to cluster-level resources and thus are typically, but not always, used for cluster configuration. You can choose to elevate certain namespace-scoped Argo CD instances to become cluster-scoped. To elevate the instances, you must change the `Subscription` resource of the GitOps Operator.

<div class="important">

<div class="title">

</div>

- Ensure you give careful consideration while elevating instances.

- Do not elevate instances that are self-managed by application delivery teams. Elevating such instances would be a severe security risk to the cluster because this action makes users of self-managed instances cluster administrators, and gives them full control over the permissions.

</div>

Much care must be taken when setting up multitenancy in Argo CD. For example, if cluster administrators manage a shared Argo CD instance for many application teams, a custom cluster-scoped instance might be appropriate.

**How does this method work?**

To prevent users from deploying Argo CD instances with `cluster-admin` privileges, you must identify the namespaces with cluster privileges by using the `ARGOCD_CLUSTER_CONFIG_NAMESPACES` environment variable in the `Subscription` resource.

Because non-cluster administrators do not have access to the `Subscription` resource, they cannot elevate the privileges of their instance and bypass cluster security.

When an instance is designated as cluster-scoped, the Operator automatically creates cluster roles and cluster role bindings. These are created for the Argo CD Application Controller and server service accounts in that namespace.

This default role is not intended to be equal to the standard `cluster-admin` role. It gives a much smaller set of permissions. You can extend these permissions by creating additional cluster roles or cluster role bindings as needed.

# Additional resources

- [Managing the application resources in non-control plane namespaces](../argocd_applications/managing-apps-in-non-control-plane-namespaces.md#managing-apps-in-non-control-plane-namespaces)

## Default cluster-scoped instance

After you install the GitOps Operator, by default, it instantiates a cluster-scoped instance in the `openshift-gitops` namespace. This instance is configured in a very opinionated way and is intended to allow cluster administrators to manage certain cluster configuration resources.

<div class="important">

<div class="title">

</div>

- Do not use the default cluster-scoped instance for anything else, such as application delivery.

- Do not grant permission to users who do not have `cluster-admin` roles to access the default cluster-scoped instance.

</div>

The default instance does not have full `cluster-admin` privileges. It has read access to all resources in the cluster, but it can only deploy a limited set of resources.

> [!NOTE]
> Use the default Argo CD instance in the `openshift-gitops` namespace for cluster configuration and delegate tenant use cases to one or many separate instances in other namespaces.

# Important considerations when adopting the multitenancy model

Granting multitenant cluster administration privileges might allow tenants to bypass any multitenancy efforts and permission restrictions because they might elevate their privileges by using permissions granted to the application by Argo CD. To prevent such situations, you must understand the permission model for Argo CD installed through the Red Hat OpenShift GitOps Operator and how to use it to be successful with OpenShift GitOps for application delivery.

## Argo CD role-based access control (RBAC)

Access controls in Red Hat OpenShift GitOps are managed at two distinct levels as follows:

- At the Kubernetes level, the GitOps Argo CD Application Controller interacts with one or more clusters to deploy various resources by using a single Kubernetes service account per cluster. This service account must have enough permissions to deploy resources for all tenants and use cases that this instance of Argo CD is managing.

- At the Argo CD level, the GitOps Argo CD Application Controller includes its own RBAC permissions model independent of Kubernetes. To manage the user-level access, you can use this RBAC model independently of the underlying Kubernetes permissions. You can use this capability to give access to Argo CD applications that a user would not have access to from a purely Kubernetes perspective.

Because these two access controls and the interaction between components are distinct and separate, privilege escalation becomes a concern when designing a multitenant solution with Argo CD. Privilege escalation is when a tenant uses the increased privileges of the application controller’s service account to perform actions they would not typically be permitted to perform. You can mitigate the privilege escalation in an Argo CD instance by using the Argo CD RBAC or separate instances of Argo CD.

## Argo CD projects

Argo CD projects, not to be confused with OpenShift Container Platform projects, provide a way to group applications together. With Argo CD projects, you can specify restrictions on Applications, such as what resources can be deployed and where they can be deployed.

Additionally, you can define Argo CD role-based access control (RBAC) rules at the project level. This approach allows more granular permissions compared to the global settings in the Argo CD custom resource (CR).

While you can define tenant RBAC globally in the Operator’s Argo CD CR, you should define tenant RBAC along with restrictions in the `AppProject` CR.

If you have a large number of tenants, attempting to manage all tenants with global RBAC might lead to much repetition.

If you have many instances of tenants, some of the project configurations might be common across tenant projects. To reduce duplication and minimize maintenance, use global projects for common configuration and inherit them in tenant projects.

> [!NOTE]
> Always define your projects and never use the default project created with an Argo CD installation by the Operator.

# Enable tenant namespace management with the NamespaceManagement CR

By default, only a cluster administrator can enable Argo CD to manage a namespace by labeling it with `argocd.argoproj.io/managed-by: <argo-cd-namespace>`. Because modifying namespaces requires cluster-admin privileges, this approach is not suitable for tenant self-service.

*NamespaceManagement CR Overview*

The namespace management feature in GitOps introduces a new `NamespaceManagement` custom resource (CR) that allows tenants to delegate control of their own namespaces to Argo CD instances without requiring direct cluster administrator action. For security reasons, this feature is disabled by default and must be explicitly enabled by a cluster administrator.

When enabled, Argo CD administrators can configure namespace management by using glob patterns to match one or more namespaces, such as `/*` or `tenant-/\*`. Tenants then create a `NamespaceManagement` custom resource (CR) in their target namespace. The Red Hat OpenShift GitOps Operator automatically provisions the required role-based access control (RBAC) resources and updates the Argo CD cluster secret, ensuring that the namespace is managed correctly.

*Effects of `NamespaceManagement` CR*

The lifecycle of a `NamespaceManagement` CR determines how the Red Hat OpenShift GitOps Operator responds:

- **Creation**: A Role and RoleBinding is created, and the namespace is added to the cluster secret.

- **Update**: RBAC and cluster secret entries are updated when the `.spec.managedBy` field changes.

- **Deletion**: The associated RBAC resources and cluster secret entries are removed.

If this feature is disabled at the `Subscription` level, all `NamespaceManagement` related configuration is cleaned up automatically.

## Configuring namespace management for Argo CD tenants

You can enable non-cluster-admin users to configure namespace management for their Argo CD instances by creating a `NamespaceManagement` custom resource (CR).

<div>

<div class="title">

Prerequisites

</div>

- You have logged in to the OpenShift Container Platform cluster as an administrator.

- You have installed the GitOps Operator on your OpenShift Container Platform cluster.

- You can access the default Argo CD instance in the `openshift-gitops` namespace.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Enable the feature in the `Subscription` Custom Resource (CR).

    Edit the Red Hat OpenShift GitOps Operator `Subscription` CR to allow namespace management.

    ``` yaml
    apiVersion: operators.coreos.com/v1alpha1
    kind: Subscription
    metadata:
      name: argocd-operator
      namespace: argocd
    spec:
      config:
        env:
        - name: ALLOW_NAMESPACE_MANAGEMENT_IN_NAMESPACE_SCOPED_INSTANCES
          value: "true"
    ```

    where:

    `spec.config.env[].name`
    Specifies the environment variable `ALLOW_NAMESPACE_MANAGEMENT_IN_NAMESPACE_SCOPED_INSTANCES` used to enable namespace management for namespace-scoped Argo CD instances.

    `spec.config.env[].value`
    Specifies the value of the environment variable. Set the value to `"true"` to enable namespace management.

2.  Configure the Argo CD CR.

    Update the Argo CD instance to allow namespace management.

    ``` yaml
    apiVersion: argoproj.io/v1alpha1
    kind: ArgoCD
    metadata:
      name: example-argocd
      namespace: <argocd_ns>
    spec:
      namespaceManagement:
        - name: <tenant_ns>
          allowManagedBy: true
    ```

    where:

    `<metadata.namespace>`
    Specifies the `<argocd_ns>` with the Argo CD instance namespace.

    `<spec.namespaceManagement.name>`
    Specifies the `<tenant_ns>` with the namespace that you want Argo CD to manage. You can also use a glob pattern, for example, use asterisks as wildcards for pattern matching.

3.  Create a `NamespaceManagement` CR.

    In the tenant namespace, the tenant user creates a `NamespaceManagement` CR:

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: NamespaceManagement
    metadata:
      name: ui-team-namespace
      namespace: <tenant_ns>
    spec:
      managedBy: <argocd_ns>
    ```

    where:

    `<metadata.namespace>`
    Specifies the namespace to be managed by the Argo CD instance.

    `<spec.managedBy>`
    Specifies the namespace where the Argo CD instance runs. This value must exactly match the Argo CD namespace.

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

After you create the `NamespaceManagement` CR, the Red Hat OpenShift GitOps Operator automatically performs the following actions:

</div>

- Creates the required `Role` and `RoleBinding` resources in the tenant namespace.

- Updates the Argo CD cluster secret to include the tenant namespace.

You can verify the following resources in the tenant namespace:

- Roles: `<argocd_instance_name>-argocd-server`, `<argocd_instance_name>-argocd-application-controller`

- RoleBindings: `<argocd_instance_name>-argocd-server`, `<argocd_instance_name>-argocd-application-controller`

- Cluster secret: `<argocd_instance_name>-cluster`

where, \<argocd_instance_name\> is the name of your Argo CD instance.

# Additional resources

- [Glossary of common terms for OpenShift GitOps](../understanding_openshift_gitops/about-redhat-openshift-gitops.md#gitops-openshift-go-common-terms_about-redhat-openshift-gitops)

- [5 global environment variables provided by Red Hat OpenShift GitOps](https://developers.redhat.com/articles/2023/03/06/5-global-environment-variables-provided-openshift-gitops#)

- [Elevating Argo CD instances to cluster-scoped instances](../declarative_clusterconfig/configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.md#configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations)

- [Understanding how to configure role-based access control (RBAC) policies](https://argo-cd.readthedocs.io/en/stable/operator-manual/rbac/)

- [Configuring global projects](https://argo-cd.readthedocs.io/en/stable/user-guide/projects/#configuring-global-projects-v18)

- [Using GitOps and Argo CD with RBAC](https://www.redhat.com/en/blog/a-guide-to-using-gitops-and-argocd-with-rbac)
