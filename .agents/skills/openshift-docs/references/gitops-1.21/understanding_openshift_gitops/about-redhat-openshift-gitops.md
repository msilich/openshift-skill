<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat OpenShift GitOps is an Operator that uses Argo CD as the declarative GitOps engine. It enables GitOps workflows across multicluster OpenShift and Kubernetes infrastructure. Using Red Hat OpenShift GitOps, administrators can consistently configure and deploy Kubernetes-based infrastructure and applications across clusters and development lifecycles.

Red Hat OpenShift GitOps is based on the open source project Argo CD. It provides similar features to the upstream project, with additional automation and integration into OpenShift Container Platform. It also includes Red Hat enterprise support, quality assurance, and a focus on enterprise security.

> [!NOTE]
> Because Red Hat OpenShift GitOps releases on a different cadence from OpenShift Container Platform, the Red Hat OpenShift GitOps documentation is now available as separate documentation sets for each minor version of the product.
>
> The Red Hat OpenShift GitOps documentation is available on Red Hat documentation and the Red Hat Customer Portal. You can use the version selector to access documentation for specific versions. For additional information about the Red Hat OpenShift GitOps life cycle and supported platforms, refer to the Platform Life Cycle Policy.

Red Hat OpenShift GitOps ensures consistency in applications when you deploy them to different clusters in different environments, such as: development, staging, and production. Red Hat OpenShift GitOps organizes the deployment process around the configuration repositories and makes them the central element. It always has at least two repositories:

1.  Application repository with the source code

2.  Environment configuration repository that defines the required state of the application

These repositories contain a declarative description of the infrastructure you need in your specified environment. They also contain an automated process to make your environment match the described state.

Red Hat OpenShift GitOps uses Argo CD to maintain cluster resources. Argo CD is an open source declarative tool for the continuous deployment (CD) of applications. Red Hat OpenShift GitOps implements Argo CD as a controller so that it continuously monitors application definitions and configurations defined in a Git repository. Then, Argo CD compares the specified state of these configurations with their live state on the cluster.

Argo CD reports any configurations that deviate from their specified state. These reports allow administrators to automatically or manually resync configurations to the defined state. Therefore, you can use Argo CD to deliver global custom resources, such as the resources that are used to configure OpenShift Container Platform clusters.

# Key features

Red Hat OpenShift GitOps automates the following tasks:

- Ensure that the clusters have similar states for configuration, monitoring, and storage

- Apply or revert configuration changes to multiple OpenShift Container Platform clusters

- Associate templated configuration with different environments

- Promote applications across clusters, from staging to production

# Glossary of common terms for OpenShift GitOps

This glossary defines common OpenShift GitOps terms.

Application Controller (Argo CD Application Controller)
A controller that performs the following actions:

- Continuously watches the Git repository for changes

- Monitors running applications

- Compares the live state against the required target state

- Deploys new changes

  Examples include Argo CD Application Controller detecting an `OutOfSync` application state and optionally taking corrective action.

`Application` custom resource (CR)
A YAML manifest that describes how to deploy the resources of your Argo CD application.

`Application` custom resource definition (CRD)
A resource object representing a deployed Argo CD application instance in an environment.

`ApplicationSet` CRD (Argo CD application set)
A resource object and a CRD that automatically generates Argo CD applications based on the contents of an `ApplicationSet` CR. Cluster administrators use this CRD to define a single `ApplicationSet` CR to generate and update multiple corresponding Argo CD `Application` CRs.

ApplicationSet Controller (Argo CD ApplicationSet Controller)
A custom Kubernetes controller that exists within Argo CD and processes `ApplicationSet` CRs. This controller automatically creates, updates, and deletes Argo CD applications based on the contents of an `ApplicationSet` CR.

`AppProject` CRD
A CRD represents a logical grouping of applications within a project that governs where and how an application is allowed to manage resources. You can use the `AppProject` CRD to restrict where and how Argo CD users are allowed to access those applications. Managing the `AppProject` instances is an action typically restricted to Argo CD administrators.

Argo CD API server
A gRPC/REST server that exposes the API consumed by the web UI, CLI, continuous integration (CI), and continuous deployment (CD) systems.

Argo CD
An open source declarative tool that automates the continuous deployment of Kubernetes-based infrastructure and applications across clusters and development lifecycles.

Argo CD application
An application that tracks the continuous deployment of individual Kubernetes resources from the GitOps repository, where the resources are defined as manifests, to a target Kubernetes cluster.

`ArgoCD` CRD
A Kubernetes CRD that describes the wanted state for a given Argo CD cluster. You can use this CRD to configure the components that make up an Argo CD cluster.

Argo CD instance
A single installation of Argo CD within a namespace that encapsulates all of the stateful aspects of a running Argo CD. Each Argo CD instance usually has a one-to-one mapping with an `ArgoCD` CR.

Argo CD project
An entity within Argo CD that refers to the Argo CD open source project’s specific concept of projects, and the corresponding `AppProject` CR.

With an Argo CD project, you can define multiple namespaces and even clusters as allowed destinations. In contrast, an OpenShift project is restricted to a single namespace and is equivalent in concept to a namespace.

Argo CD project controls the behavior of Argo CD by restricting access to Git repositories and remote clusters. Examples include using the Argo CD project to control users by restricting who can access certain Argo CD applications or cluster resources through the Argo CD UI or Argo CD CLI.

Argo CD repository server (Argo CD-repo-server)
An Argo CD component that performs the following actions:

- Reads from source repositories such as Git, Helm, or Open Container Initiative (OCI)

- Generates corresponding application manifests

- Runs custom configuration management tools

- Returns the result to the Argo CD Application Controller

Argo CD resource (`ArgoCD` CR)
A CR that describes the wanted state for a given Argo CD instance. You can use this CR to configure the components and settings that make up an Argo CD instance. At any given time, you can have only one `ArgoCD` CR within a namespace.

Argo CD server (Argo CD-server)
A server that provides the API and UI for Argo CD.

Argo Rollouts
A controller that you can use for managing the progressive deployment of applications hosted on Kubernetes and OpenShift Container Platform clusters. This controller has a set of CRDs that provides advanced deployment capabilities such as blue-green, canary, canary analysis, and experimentation.

Cluster-scoped instance
A mode where you configure Argo CD to manage all resources on the cluster including certain cluster-specific resources such as cluster configuration, cluster RBAC, Operator resources, platform Operators, or secrets.

Control plane (GitOps control plane)
In the GitOps context, you can have a control plane for every Argo CD you install. A GitOps control plane is any namespace where you can install Argo CD. With this control plane, you can provision, manage, and operate Argo CD across networks, instances, and clusters.

Within a control plane namespace, Argo CD maintains the following set of Kubernetes resources, which define the continuous deployment between the source Git repository and destination clusters:

- Argo CD `Application` CRs

- `ConfigMap` API objects

- `Secret` objects representing the GitOps repository credentials and cluster credentials for deployment targets

  `openshift-gitops` is the control plane namespace for the default Argo CD instance.

Declarative setup
A declarative description of the infrastructure required in your specified environment, for system and application setup or configuration. You can specify this description in a YAML configuration file in the Git repository. The declarative setup contains an automated process to make your environment and infrastructure match the described state. Examples include defining Argo CD applications, projects, and settings declaratively by using YAML manifests.

Default Argo CD instance (Default cluster-scoped instance)
A default instance that a Red Hat OpenShift GitOps Operator instantiates immediately after its installation, in the `openshift-gitops` namespace, with additional permissions for managing certain cluster-scoped resources.

GitOps
A declarative way to implement continuous deployment for cloud native applications. In GitOps, a Git repository contains deployment resources, which Argo CD keeps synchronizing with its cluster state.

GitOps CLI (GitOps `argocd` CLI)
A tool to configure and manage Red Hat OpenShift GitOps and Argo CD resources from the command line.

Instance scopes
Modes that determine how you want to operate an Argo CD instance. The available modes are *cluster-scoped instance* and *namespace-scoped instance*.

Live state
The live state of application resources on a target cluster.

Local cluster
A cluster where you install Argo CD.

Manifest
In the GitOps context, a manifest is a YAML representation of Kubernetes resources defined within a GitOps repository, with the intent to deploy those resources to a target Kubernetes cluster. Examples include the YAML representation of resources such as `Deployment`, `ConfigMap`, or `Secret`.

Multitenancy
A software architecture where a single software instance serves multiple distinct user groups.

Namespace-scoped instance (Application delivery instance)
A mode in which Argo CD is configured to manage resources in only certain namespaces on a cluster and use the resources for application delivery.

Notifications Controller (Argo CD Notifications Controller)
A controller that continuously monitors Argo CD applications and provides a flexible way to notify users about important changes in the application state.

Progressive delivery
In the GitOps context, progressive delivery is a process of releasing application updates in a controlled and gradual manner.

Red Hat OpenShift GitOps
An Operator that uses Argo CD as the declarative GitOps engine to enable GitOps workflows across multicluster OpenShift and Kubernetes infrastructures.

Refresh
The process of comparing the latest code in the Git repository with the live state and determining the difference. For example, in the Argo CD UI, when you click **Refresh**, Argo CD connects to an application’s target Git repository, retrieves the content, and then generates manifests from that content. Argo CD then compares that target state against the live cluster state.

Remote cluster
A cluster that you can add to Argo CD either declaratively or by using the GitOps CLI. Remote cluster is distinct from the local cluster where Argo CD is installed.

Resource Exclusion
A configuration you use to exclude resources from discovery and sync so that Argo CD is unaware of them.

Resource Inclusion
A configuration you use to include resources to discover, sync, and restrict the list of managed resources globally.

Single tenancy
A software architecture where a single software instance serves a single user or group of users.

Sync
The process of synchronizing the live state of an application’s cluster resources with the target state defined within the Git repository to ensure consistency. Examples include syncing an application by applying changes to a cluster by using the Argo CD UI.

Sync status
The status of an application that indicates whether the live state matches the target state.

Target state
The wanted state of application resources, as represented by files in a Git repository.

User-defined Argo CD instance
A custom Argo CD instance that you install and deploy to manage cluster configurations or deploy applications. By default, any new user-defined instance has permissions to manage resources only in the namespace where it is deployed.

You can create a user-defined Argo CD instance in any namespace, other than the `openshift-gitops` namespace.

Workload
Any process, usually defined within resources such as `Deployment`, `StatefulSet`, `ReplicaSet`, `Job`, or `Pod`, running within a container. Examples include a Spring Boot application, a NodeJS Express application, or a Ruby on Rails application.

<div>

<div class="title">

Additional resources

</div>

- [Argo CD projects](https://argo-cd.readthedocs.io/en/stable/user-guide/projects)

- [AppProject CR declarative setup](https://argo-cd.readthedocs.io/en/stable/operator-manual/declarative-setup/#projects)

- [OpenShift common terms](https://docs.openshift.com/container-platform/latest/getting_started/openshift-overview.html#getting-started-openshift-common-terms_openshift-overview)

</div>

# Additional resources

- [Extending the Kubernetes API with custom resource definitions](https://docs.openshift.com/container-platform/latest/operators/understanding/crds/crd-extending-api-with-crds.html#crd-extending-api-with-crds)

- [Managing resources from custom resource definitions](https://docs.openshift.com/container-platform/latest/operators/understanding/crds/crd-managing-resources-from-crds.html#crd-managing-resources-from-crds)

- [What is GitOps?](what-is-gitops.md#what-is-gitops)

- [What is an OpenShift project?](https://docs.openshift.com/container-platform/latest/getting_started/openshift-overview.html#getting-started-openshift-common-terms_openshift-overview)

- [Specification of an `AppProject` CRD](https://argo-cd.readthedocs.io/en/stable/operator-manual/project-specification)

- [Argo CD](https://argoproj.github.io/cd/)

- [Red Hat OpenShift GitOps documentation](https://docs.redhat.com/en/documentation/red_hat_openshift_gitops/)

- [Red Hat OpenShift GitOps documentation on Red Hat Customer Portal](https://access.redhat.com/documentation/en-us/red_hat_openshift_gitops/)

- [Platform Life Cycle Policy](https://access.redhat.com/support/policy/updates/openshift#gitops)
