<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

> [!IMPORTANT]
> GitOps Console plugin is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

The GitOps Console plugin extends the OpenShift Container Platform web console by adding GitOps resources. The plugin is available as part of the Red Hat OpenShift GitOps Operator and provides a console UI for managing Argo CD and Argo Rollouts custom resources.

After you install the Red Hat OpenShift GitOps Operator and enable the GitOps Console plugin, the Red Hat OpenShift GitOps web console displays a **GitOps** navigation tab in the **Administrator** perspective. The GitOps navigation tab replaces the previous **Environments** tab and related pages in the **Developer** perspective.

The GitOps navigation tab provides access to the following Argo CD and Argo Rollouts resources:

- Applications

- ApplicationSets

- AppProjects

- Rollouts

# Prerequisites

- You have access to OpenShift Container Platform 4.19 or later.

- You have installed the Red Hat OpenShift GitOps Operator.

# GitOps resources in the web console

Each GitOps resource provides list and details pages that follow the standard Red Hat OpenShift GitOps web console experience.

You can use these pages to:

- View GitOps resources in a selected namespace

- Create resources by using YAML templates

- Edit labels and annotations

- Filter resources by status, where applicable

- Access related resources and events

The GitOps Console plugin integrates with the console navigation, allowing you to navigate between related resources and access contextual actions for each resource type.

## Search and YAML templates

The GitOps Console plugin provides search and template capabilities:

- **Search integration**: Search pages are enabled for Applications and ApplicationSets, allowing you to find instances from global search like other first-class resources.

- **YAML templates**: Pre-configured YAML templates are registered for Applications, ApplicationSets, AppProjects, and Rollouts. These templates provide starter configurations with placeholders to speed up resource creation from the console.

# Enable the GitOps Console plugin

If you disable the GitOps Console plugin after installing the Red Hat OpenShift GitOps Operator, you can enable it manually.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Red Hat OpenShift GitOps Operator.

- You have access to the Red Hat OpenShift GitOps web console with cluster administrator permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the Red Hat OpenShift GitOps web console, navigate to **Home** → **Overview**.

2.  In the **Status** panel, click **Dynamic Plugins**.

    A popup appears with a link to view all dynamic plugins.

3.  Click **View all**.

4.  Under the **Console plugins** tab, find **gitops-plugin**.

5.  If the plugin is disabled, click **Enable**.

    The browser might require a refresh. After refreshing, the page indicates that the plugin is **Enabled**.

</div>

<div>

<div class="title">

Verification

</div>

- Navigate to **GitOps** in the navigation menu and verify that you can access Applications, ApplicationSets, AppProjects, and Rollouts pages.

</div>

## Applications in the GitOps Console

The GitOps Console Plugin shows key details of an Argo CD Application. You can view and create Application directly from the OpenShift Container Platform web console. A new **Graphical view** in the **Resources** tab of the Details page shows the application’s resources in a tree structure.

> [!IMPORTANT]
> The GitOps Console plugin displays the health status stored in the Application custom resource (CR). By default, this behavior depends on the configuration set by the Operator. If the Application CR does not contain the health status or the GitOps Console plugin does not display it correctly, set `controller.resource.health.persist: "true"` in the `argocd-cmd-params-cm` config map.

**List page**

The Applications list page displays all Applications with the following features:

- **Table columns**: name, namespace, sync status, health, revision, AppProject, and actions

- **Filtering**: Filter Applications by health status (Healthy, Progressing, Degraded, Missing) and sync status (Synced, OutOfSync, Unknown)

- **Sorting and search**: Sort columns and search by name

- **Create action**: Click **Create Application** to open the YAML editor with a starter template that includes repository URL, destination, and sync policy placeholders

- **Technology Preview badge**: The feature is labeled as Technology Preview when viewed from user namespaces. When accessed from the GitOps Operator namespace (`openshift-gitops`), the badge might not appear.

- **Namespace view**: From the GitOps Operator namespace path, an optional control can list operands in all namespaces for operator-focused workflows

**Details page**

The Application details page provides the following tabs:

- **Details tab**: Displays summary information, health and sync indicators, revision links, destination and project information, conditions, toggles for automated sync, self-heal, and prune (when you have update permission), and detection of an Argo CD Route so you can open the Argo CD UI for the same application when routing is configured.

- **YAML tab**: Provides a live manifest editor for the Application resource.

- **Sources tab**: Displays repository sources with icons and metadata for Helm, Git, and OCI sources.

- **Resources tab**: Combines a resource table with an interactive topology graph:

  - The graph shows immediate managed resources for the Application, not the full Argo CD resource tree.

  - Use the Argo CD link on the tab to open the complete resource hierarchy in the Argo CD UI.

  - Pan, zoom, and select resources in the graph; status filters apply to both table and graph.

  - Context-menu actions on graph nodes include viewing details, editing labels and annotations, deleting resources, and viewing resources in Argo CD.

  - Related resources of the same kind can be grouped or ungrouped in the graph.

- **Sync Status tab**: Provides fine-grained sync and operation status information for the Application.

- **History tab**: Displays the deployment and sync history for the Application.

- **Events tab**: Shows Kubernetes events for the Application object.

**Additional features**

- **Favorites**: You can mark Applications as favorites based on console user settings.

- **Standard actions**: The page header provides access to standard actions such as editing labels, annotations, and deleting the Application.

## ApplicationSets in the GitOps Console

The GitOps Console Plugin shows key details of Argo CD ApplicationSets. You can view and create ApplicationSets directly from the OpenShift Container Platform web console. A new Graphical view shows the applications managed by an ApplicationSet and the progressive sync flow from one step to the next.

**List page**

The ApplicationSets list page follows the same list patterns as other custom resources:

- **Table columns**: Standard columns for custom resources

- **Filtering**: Filter ApplicationSets by health status (Healthy, Error, Unknown)

- **Create action**: Click **Create ApplicationSet** to open the YAML editor with a default ApplicationSet template

**Details page**

The ApplicationSet details page provides the following tabs:

- **Details tab**: Displays status information, generator counts, conditions, links to the Generators and Applications tabs, and shows the number of generated applications of related Applications.

- **YAML tab**: Provides a live manifest editor for the ApplicationSet resource.

- **Generators tab**: Provides a structured view of generator configuration, including list, merge, and union generators.

- **Applications tab**: Displays the list of applications generated by the ApplicationSet with a Graphical View showing visual representation of the generated applications, progressive sync visualization that shows the progressive sync flow from step to step when progressive sync is enabled, a filter widget to filter by health and sync status, and an applications table with the same rich columns as the main Application list page.

- **Events tab**: Shows Kubernetes events for the ApplicationSet object.

## AppProjects in the GitOps Console

The GitOps Console plugin provides summary details for Argo CD AppProjects. You can view and create project-scoped AppProjects directly from the OpenShift web console.

**List page**

The AppProjects list page displays all project-scoped AppProjects with the following features:

- **Table columns**: Standard columns for custom resources

- **Filtering**: Filter projects by Description, Applications, Project Type, Source Repositories, and Destinations

- **Create action**: Click **Create AppProject** to open the YAML editor with a default AppProject template

**Details page**

The AppProject details page provides the following tabs:

- **Details tab**: Displays project summary, destinations, policies, and related metadata.

- **YAML tab**: Provides a live manifest editor for the AppProject resource.

- **Allow/Deny tab**: Displays resource allow and deny lists for cluster-scoped and namespace-scoped kinds.

- **Applications tab**: Shows Applications that belong to this project. The table provides the same experience as the main Application list, filtered by project.

- **Roles tab**: Displays Argo CD project roles and bindings.

- **Sync Windows tab**: Shows configured sync windows for the project.

- **Events tab**: Shows Kubernetes events for the AppProject object.

## Rollouts in the GitOps Console

The GitOps Console plugin provides comprehensive details of Argo Rollouts instances in the cluster. You can view and create, Rollout resources directly from the OpenShift web console.

**List page**

The Rollouts list page displays all Argo Rollout resources with the following features:

- **Table columns**: Standard columns for Rollout resources

- **Filtering**: Filter Rollouts by rollout status (Healthy, Paused, Progressing, Degraded)

- **Create action**: Click **Create Rollout** to open the YAML editor with a default Rollout template

**Topology integration**

The OpenShift Console Topology view shows the cluster’s Rollout instances. The Topology view provides:

- Rollout Details and Overview sidebar tabs with information on the resource

- Context actions for Rollout resources

- Visual decorator on Rollout nodes

**Details page**

The Rollout details page provides the following tabs:

- **Details tab**: Displays replicas with inline scale controls when you have the required permissions, rollout status, conditions, strategy-specific sections for Canary or Blue-Green services, a link to open this workload in the Topology view, and related navigation helpers.

- **YAML tab**: Provides a live manifest editor for the Rollout resource.

- **Revisions tab**: Displays ReplicaSet and revision-oriented information for the rollout, including:

  - Rollout status and strategy

  - Revision history with ReplicaSet details

  - Pod status and health

    This view provides the same information as the oc argo rollouts get rollout CLI command, including the functionality of the --watch option, allowing you to monitor rollout progress directly from the console. For more information, see *Using Argo Rollouts for progressive deployment delivery* in Additional resources.

- **Pods tab**: Shows pods for the rollout with pod-level actions.

- **Events tab**: Shows Kubernetes events for the Rollout object.

# Filter resources

The GitOps Console plugin provides filters to narrow the resource list based on specific properties. The available filter options vary by resource type.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the Red Hat OpenShift GitOps web console.

- The GitOps Console plugin is enabled.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the Red Hat OpenShift GitOps web console, navigate to **GitOps** and select a resource type.

2.  On the list page, use the available filter controls to narrow the displayed resources.

    The following filters are available depending on the resource type:

    - **Applications**: Filter by health status (Healthy, Progressing, Degraded, Missing) and sync status (Synced, OutOfSync, Unknown).

    - **ApplicationSets**: Filter by health status (Healthy, Error, Unknown).

    - **AppProjects**: Filter by Description, Applications, Project Type, Source Repositories, and Destinations.

    - **Rollouts**: Filter by rollout status (Healthy, Paused, Progressing, Degraded).

3.  Optional: Combine multiple filters to narrow the results further.

4.  To clear filters, click the **Clear all filters** link or remove individual filter selections.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the resource list displays only items matching your selected filter criteria.

</div>

# Additional resources

- [Deploying a Spring Boot application with Argo CD](deploying-a-spring-boot-application-with-argo-cd.md#deploying-a-spring-boot-application-with-argo-cd)

- [Managing application sets in non-control plane namespaces](../argocd_application_sets/managing-app-sets-in-non-control-plane-namespaces.md#managing-app-sets-in-non-control-plane-namespaces)

- [Multitenancy support in GitOps](../multitenancy/multitenancy-support-in-gitops.md#multitenancy-support-in-gitops)

- [Using Argo Rollouts for progressive deployment delivery](../argo_rollouts/using-argo-rollouts-for-progressive-deployment-delivery.md#using-argo-rollouts-for-progressive-deployment-delivery)

- [Argo CD Documentation](https://argo-cd.readthedocs.io/en/stable/)

- [Argo Rollouts Documentation](https://argo-rollouts.readthedocs.io/en/stable/)
