<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

By default, Red Hat OpenShift GitOps installs an instance of Argo CD in the `openshift-gitops` namespace with additional permissions for managing certain cluster-scoped resources. This default Argo CD instance is also called as the default cluster-scoped instance.

To prevent the default Argo CD instance from starting in the `openshift-gitops` namespace, you can use the `openshift-gitops-operator` subscription and configure the `DISABLE_DEFAULT_ARGOCD_INSTANCE` environment variable in it by setting the string value to `"true"`.

> [!NOTE]
> For GitOps version 1.13 and later:
>
> - The default Route TLS termination mode is `reencrypt` for both default and user-defined Argo CD instances. TLS connections to Argo CD instances now use the default ingress certificate configured in OpenShift Container Platform instead of the self-signed Argo CD certificate. To change the route TLS termination policy, configure the `.spec.server.route.tls` field in the Argo CD CR.
>
> - Restricted pod security admission (PSA) labels are applied to the `openshift-gitops` namespace to ensure compliance with OpenShift Container Platform standards. If you are running additional workloads in this namespace, such as monitoring or logging, ensure that they comply with the restricted PSA requirements. If compliance is not feasible, consider using a user-defined, cluster-scoped Argo CD instance, where PSA labels are not applied or controlled by the GitOps Operator.

To manage cluster configurations or deploy applications, you can install and deploy a new user-defined Argo CD instance. By default, any new user-defined instance has permissions to manage resources only in the namespace where it is deployed.

<div class="warning">

<div class="title">

</div>

- A Kubernetes user with access to the Argo CD namespace is an Argo CD administrator and can bypass any role-based access control (RBAC) restrictions configured in Argo CD. Never grant non-administrator users any read or write access to the Argo CD namespace.

- If non-administrator users create applications, do not allow them to bind to the default `AppProject` custom resource (CR) because it has no restrictions. Otherwise, the Kubernetes permissions of the Argo CD instance and the default `AppProject` CR can allow deployment of anything to any location. To avoid this risk, lock down the default `AppProject` CR so no one can use it by mistake, even if the Argo CD RBAC is misconfigured.

</div>

You can create a user-defined Argo CD instance in any namespace, other than the `openshift-gitops` namespace.

> [!IMPORTANT]
> If you want to create a user-defined Argo CD instance within the `openshift-gitops` namespace, set the `DISABLE_DEFAULT_ARGOCD_INSTANCE` flag value in the `openshift-gitops-operator` subscription to `"true"` and do not name the instance as `openshift-gitops`.

# Installing a user-defined Argo CD instance

To manage cluster configurations or deploy applications, you can install and deploy a new user-defined Argo CD instance.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  In the **Administrator** perspective of the web console, click **Operators** → **Installed Operators**.

3.  Create or select the project where you want to install the user-defined Argo CD instance from the **Project** list.

4.  Select **Red Hat OpenShift GitOps** from the installed Operators list and click the **Argo CD** tab.

5.  Click **Create ArgoCD** to configure the parameters:

    1.  Enter the **Name** of the instance. By default, the **Name** is set to `example`.

    2.  Create an external operating system Route to access Argo CD server. Click **Server** → **Route** and check **Enabled**.

        > [!TIP]
        > You can alternatively configure YAML to create an external OS Route as shown in the following example:
        >
        > **Example Argo CD with external OS route created:**
        >
        > ``` yaml
        > apiVersion: argoproj.io/v1beta1
        > kind: ArgoCD
        > metadata:
        >   name: example
        >   namespace: openshift-gitops
        > spec:
        >   server:
        >     route:
        >       enabled: true
        > ```

    3.  Optional: Change the route TLS termination policy by configuring the `.spec.server.route.tls` field of the Argo CD CR.

        > [!NOTE]
        > When configuring custom TLS certificates for Argo CD Server route, avoid using the `.spec.server.route.tls.key` and `.spec.server.route.tls.certificate` fields. Use the `.spec.server.route.tls.externalCertificate` field instead. For more information about configuring a route for custom TLS certificate, see examples in [Custom TLS certificates for Routes](https://argocd-operator.readthedocs.io/en/latest/usage/routes/#custom-tls-certificates).

6.  Click **Create**.

7.  Go to **Networking** → **Routes** → **\<instance_name\>-server** in the project where the user-defined Argo CD instance is installed.

8.  On the **Details** tab, click the Argo CD web UI link under **Route details** → **Location**. The Argo CD web UI opens in a separate browser window.

9.  Optional: To log in with your OpenShift Container Platform credentials, ensure you are a user of the `cluster-admins` group and then select the `LOG IN VIA OPENSHIFT` option in the Argo CD user interface.

    > [!NOTE]
    > To be a user of the `cluster-admins` group, use the `oc adm groups new cluster-admins <user>` command, where `<user>` is the default cluster role that you can bind to users and groups cluster-wide or locally.

10. Obtain the password for the user-defined Argo CD instance:

    1.  Use the navigation panel to go to the **Workloads** → **Secrets** page.

    2.  Use the **Project** list and select the namespace where the user-defined Argo CD instance is created.

    3.  Select the **\<argo_CD_instance_name\>-cluster** instance to display the password.

    4.  On the **Details** tab, copy the password under **Data** → **admin.password**.

11. Use `admin` as the **Username** and the copied password as the **Password** to log in to the Argo CD UI in the new window.

</div>

# Additional resources

- [Configuring the route TLS termination](https://argocd-operator.readthedocs.io/en/latest/usage/routes/#setting-tls-modes-for-routes)

- [Argo CD custom resource properties](argo-cd-cr-component-properties.md#argo-cd-properties_argo-cd-cr-component-properties)

- [Specification for TLS termination configuration](https://docs.openshift.com/container-platform/latest/rest_api/network_apis/route-route-openshift-io-v1.html#spec-tls)

- [Persistent volumes for repo server storage](https://argocd-operator.readthedocs.io/en/latest/usage/ha/repo-server)

- [Using an Argo CD instance to manage cluster-scoped resources](../declarative_clusterconfig/configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.md#using-argo-cd-instance-to-manage-cluster-scoped-resources_configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations)

- [Disabling the creation of the default cluster roles for the cluster-scoped instance](../declarative_clusterconfig/customizing-permissions-by-creating-user-defined-cluster-roles-for-cluster-scoped-instances.md#gitops-disabling-the-creation-of-the-default-cluster-roles-for-the-cluster-scoped-instance_customizing-permissions-by-creating-user-defined-cluster-roles-for-cluster-scoped-instances)

- [Configuring Argo CD controller options](https://argocd-operator.readthedocs.io/en/stable/reference/argocd/#controller-options)

- [Configuring Argo CD server options](https://argocd-operator.readthedocs.io/en/stable/reference/argocd/#server-options)

# Configuring common cluster roles by specifying user-defined cluster roles for namespace-scoped instances

As a cluster administrator, when you give an Argo CD access to a namespace by using the `argocd.argoproj.io/managed-by` label, the Argo CD assumes `namespace-admin` privileges. The Red Hat OpenShift GitOps Operator then automatically creates role bindings for all managed namespaces of the following GitOps control plane components:

- Argo CD Application Controller

- Argo CD server

- Argo CD `ApplicationSet` Controller

When you give namespaces to non-administrator users, for example, development teams, they can use the `namespace-admin` privileges to modify objects such as network policies. Installing an Argo CD instance in these namespaces gives the development teams `admin` privileges and indirectly elevates their assigned privileges. These roles are highly privileged and can delete all resources. To reduce this risk, configure common cluster roles with limited permissions in the role bindings that the Operator creates for the Argo CD Application Controller and Argo CD server.

To configure common cluster roles for all managed namespaces, you can specify user-defined cluster roles for the `CONTROLLER_CLUSTER_ROLE` and `SERVER_CLUSTER_ROLE` environment variables in the Operator’s `Subscription` object YAML file. As a result, instead of creating the default `admin` role, the Operator uses the existing user-defined cluster roles and creates role bindings for all managed namespaces.

<div>

<div class="title">

Prerequisites

</div>

- You have logged in to the OpenShift Container Platform cluster as an administrator.

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the **Administrator** perspective, navigate to **Administration** → **CustomResourceDefinitions**.

2.  Find the **Subscription** custom resource definition (CRD) and click to open it.

3.  Select the **Instances** tab and click the **openshift-gitops-operator** subscription.

4.  Select the **YAML** tab and make your customization:

    - Specify the user-defined cluster roles for the `CONTROLLER_CLUSTER_ROLE` and `SERVER_CLUSTER_ROLE` environment variables:

      **Example Subscription:**

      ``` yaml
      apiVersion: operators.coreos.com/v1alpha1
      kind: Subscription
      metadata:
        name: openshift-gitops-operator
        namespace: openshift-gitops-operator
      spec:
        config:
          env:
          - name: CONTROLLER_CLUSTER_ROLE
            value: gitops-controller-role
          - name: SERVER_CLUSTER_ROLE
            value: gitops-server-role
      ```

      where:

      `metadata.name`
      Specifies the name of the `Subscription` resource.

      `metadata.namespace`
      Specifies the namespace where the `Subscription` resource is created.

      `spec.config.env`
      Specifies environment variables that are passed to the Operator.

      `spec.config.env[].name`
      Specifies the name of the environment variable.

      `spec.config.env[].value`
      Specifies the value assigned to the environment variable.

      > [!TIP]
      > You can also inject the preceding environment variables directly into the Operator’s `Deployment` object YAML file.

</div>

# Additional resources

- [Customizing permissions by creating user-defined cluster roles for cluster-scoped instances](../declarative_clusterconfig/customizing-permissions-by-creating-user-defined-cluster-roles-for-cluster-scoped-instances.md#customizing-permissions-by-creating-user-defined-cluster-roles-for-cluster-scoped-instances)

- [Customizing permissions by creating aggregated cluster roles](../declarative_clusterconfig/customizing-permissions-by-creating-aggregated-cluster-roles.md#customizing-permissions-by-creating-aggregated-cluster-roles)

# Enabling replicas for Argo CD server and repo server

Argo CD-server and Argo CD-repo-server workloads are stateless. To better distribute your workloads among pods, you can increase the number of Argo CD-server and Argo CD-repo-server replicas. However, if a horizontal autoscaler is enabled on the Argo CD-server, it overrides the number of replicas you set.

<div>

<div class="title">

Procedure

</div>

- Set the `replicas` parameters for the `repo` and `server` spec to the number of replicas you want to run:

  **Example Argo CD custom resource:**

  ``` yaml
  apiVersion: argoproj.io/v1beta1
  kind: ArgoCD
  metadata:
    name: example-argocd
    labels:
      example: repo
  spec:
    repo:
      replicas: <number_of_replicas>
    server:
      replicas: <number_of_replicas>
      route:
        enabled: true
        path: /
        tls:
          insecureEdgeTerminationPolicy: Redirect
          termination: passthrough
        wildcardPolicy: None
  ```

</div>

# Deploying resources to a different namespace

To allow Argo CD to manage resources in other namespaces apart from where it is installed, configure the target namespace with a `argocd.argoproj.io/managed-by` label.

<div>

<div class="title">

Procedure

</div>

- Configure the target namespace by running the following command:

  ``` terminal
  $ oc label namespace <target_namespace> \
  argocd.argoproj.io/managed-by=<argocd_namespace>
  ```

  where:

  `<target_namespace>`
  Specifies the name of the namespace you want Argo CD to manage.

  `<argocd_namespace>`
  Specifies the name of the namespace where Argo CD is installed.

</div>

# Customizing the Argo CD console link

In a multitenant cluster, users might have to deal with many instances of Argo CD. After installing an Argo CD instance in your namespace, the Argo CD console link in the Console Application Launcher might open another Argo CD instance.

You can customize the Argo CD console link by setting the `DISABLE_DEFAULT_ARGOCD_CONSOLELINK` environment variable:

- When you set `DISABLE_DEFAULT_ARGOCD_CONSOLELINK` to `true`, the Argo CD console link is permanently deleted.

- When you set `DISABLE_DEFAULT_ARGOCD_CONSOLELINK` to `false` or use the default value, the Argo CD console link is temporarily deleted and visible again when the Argo CD route is reconciled.

<div>

<div class="title">

Prerequisites

</div>

- You have logged in to the OpenShift Container Platform cluster as an administrator.

- You have installed the Red Hat OpenShift GitOps Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the **Administrator** perspective, navigate to **Administration** → **CustomResourceDefinitions**.

2.  Find the **Subscription** CRD and click to open it.

3.  Select the **Instances** tab and click the **openshift-gitops-operator** subscription.

4.  Select the **YAML** tab and make your customization:

    - To enable or disable the Argo CD console link, edit the value of `DISABLE_DEFAULT_ARGOCD_CONSOLELINK` as needed:

      ``` yaml
      apiVersion: operators.coreos.com/v1alpha1
      kind: Subscription
      metadata:
        name: openshift-gitops-operator
      spec:
        config:
          env:
          - name: DISABLE_DEFAULT_ARGOCD_CONSOLELINK
            value: 'true'
      ```

</div>

# Configuring ImagePullPolicy

The GitOps Operator lets administrators configure `imagePullPolicy` at multiple levels to control how Argo CD components pull container images.

The `imagePullPolicy` configuration follows a hierarchical precedence system, where the most specific configuration takes priority:

- `Instance-level policy` - Defined in the Argo CD CR by using the `spec.imagePullPolicy` field.

- `Global-level policy` - Defined through the `IMAGE_PULL_POLICY` environment variable in the GitOps Operators `Subscription`.

- `Default policy` - `IfNotPresent` is used when neither of the earlier configurations are specified.

| Value          | Description                                       |
|----------------|---------------------------------------------------|
| `Always`       | Always pull the image.                            |
| `IfNotPresent` | Pull the image only if it is not present locally. |
| `Never`        | Never pull the image.                             |

You can define a global image pull policy for all Argo CD instances managed by the Operator by setting the `IMAGE_PULL_POLICY` environment variable in the Operator’s `Subscription`. For example:

``` yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-gitops-operator
spec:
  config:
    env:
      - name: IMAGE_PULL_POLICY
        value: "Always"
```

An instance-level configuration overrides the Operator-level policy and applies the configuration only to the specific instance defined in the CR.

The following example shows how to configure `imagePullPolicy` for all the components in an Argo CD instance.

``` yaml
apiVersion: argoproj.io/v1beta1
kind: ArgoCD
metadata:
  name: argocd
  namespace: argocd
spec:
  imagePullPolicy: IfNotPresent
```

The following example shows how to define `imagePullPolicy` for all the components in a `GitOpsService` instance.

``` yaml
apiVersion: pipelines.openshift.io/v1alpha1
kind: GitOpsService
metadata:
  name: gitops-service
  namespace: openshift-gitops
spec:
  imagePullPolicy: Always
```

The following example shows how to set `imagePullPolicy` for all the components in a `RolloutsManager` instance.

``` yaml
apiVersion: argoproj.io/v1alpha1
kind: RolloutManager
metadata:
  name: argo-rollout
  labels:
    example: basic
spec:
  imagePullPolicy: Always
```

By configuring the `imagePullPolicy` at an appropriate level, you can control how often container images are updated for your GitOps components.
