<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use the Red Hat Advanced Cluster Security for Kubernetes search feature to quickly find the resources that you need to safeguard your cluster, such as deployments exposed to a newly published Common Vulnerabilities and Exposures (CVE) or deployments with external network exposure.

<a id="search-syntax_search-filter"></a>

# Search syntax

A search query consists of an attribute that identifies the resource type and a search term that finds the matching resource.

For example, to find all violations in the `visa-processor` deployment, the search query is `Deployment:visa-processor`. In this search query, `Deployment` is the attribute and `visa-processor` is the search term.

> [!NOTE]
> You must select an attribute before you can use search terms. However, in some views, such as the **Risk** view and the **Violations** view, Red Hat Advanced Cluster Security for Kubernetes automatically applies the relevant attribute based on the search term you enter.

- You can use many attributes in your query. When you use more than one attribute, the results only include the items that match all attributes.

  When you search for `Namespace:frontend CVE:CVE-2018-11776`, it returns only those resources that violate CVE-2018-11776 in the `frontend` namespace.

- You can use more than one search term with each attribute. When you use more than one search term, the results include all items that match any of the search terms.

  If you use the search query `Namespace: frontend backend`, it returns matching results from the namespace `frontend` or `backend`.

- You can combine many attribute and search term pairs.

  The search query `Cluster:production Namespace:frontend CVE:CVE-2018-11776` returns all resources that violate CVE-2018-11776 in the `frontend` namespace in the `production` cluster.

- Search terms can be part of a word, in which case Red Hat Advanced Cluster Security for Kubernetes returns all matching results.

  If you search for `Deployment:def`, the results include all deployments starting with `def`.

- To explicitly search for a specific term, use the search terms inside quotes.

  When you search for `Deployment:"def"`, the results only include the deployment `def`.

- You can also use regular expressions by using `r/` before your search term.

  When you search for `Namespace:r/st.*x`, the results include matches from namespace `stackrox` and `stix`.

- Use `!` to indicate the search terms that you do not want in results.

  If you search for `Namespace:!stackrox`, the results include matches from all namespaces except the `stackrox` namespace.

- Use the comparison operators `>`, `<`, `=`, `>=`, or `<=` to match a specific value or range of values.

  If you search for `CVSS:>=6`, the results include all vulnerabilities with Common Vulnerability Scoring System (CVSS) score 6 or higher.

<a id="search-autocomplete_search-filter"></a>

# Search autocomplete

As you enter your query, Red Hat Advanced Cluster Security for Kubernetes automatically displays relevant suggestions for the attributes and the search terms.

<a id="use-global-search_search-filter"></a>

# Using global search

By using global search, you can search across all resources in your environment. Based on the resource type you use in your search query, Red Hat Advanced Cluster Security for Kubernetes groups the results in the following categories:

- All results, which lists the matching results across all categories

- Clusters

- Deployments

- Images

- Namespaces

- Nodes

- Policies

- Policy categories <sup>\[1\]</sup>

- Roles

- Role bindings

- Secrets

- Service accounts

- Users and groups

- Violations

1.  The **Policy categories** option is only available if you use the following:

    - PostgreSQL as a backend database in Red Hat Advanced Cluster Security for Kubernetes (RHACS).

    - Red Hat Advanced Cluster Security Cloud Service (RHACS Cloud Service).

The RHACS portal global search page displays these categories as a table, and you can click the category name to identify results belonging to the selected category.

To do a global search, in the RHACS portal, select **Search**.

<a id="use-local-page-filtering_search-filter"></a>

# Using local page filtering

You can use local page filtering from within all views in the RHACS portal. Local page filtering works like global search, but only relevant attributes are available. You can select the search bar to show all available attributes for a specific view.

<a id="common-search-queries_search-filter"></a>

# Common search queries

You can use Red Hat Advanced Cluster Security for Kubernetes to run common search queries for finding deployments, vulnerabilities, and users or groups in your environment.

<a id="finding-deployments-that-are-affected-by-a-specific-cve_search-filter"></a>

## Finding deployments affected by a specific CVE

You can search for deployments that a specific Common Vulnerabilities and Exposures (CVE) affects.

| Query              | Example              |
|--------------------|----------------------|
| `CVE:<CVE_number>` | `CVE:CVE-2018-11776` |

Search query for finding deployments affected by a specific CVE

<a id="finding-privileged-running-deployments_search-filter"></a>

## Finding privileged running deployments

You can search for deployments that are running in privileged mode.

| Query                        | Example           |
|------------------------------|-------------------|
| `Privileged:<true_or_false>` | `Privileged:true` |

Search query for finding privileged running deployments

<a id="finding-deployments-that-have-external-network-exposure_search-filter"></a>

## Finding deployments that have external network exposure

You can search for deployments that have a specific level of network exposure.

| Query                    | Example                   |
|--------------------------|---------------------------|
| `Exposure Level:<level>` | `Exposure Level:External` |

Search query for finding deployments with external network exposure

<a id="finding-deployments-that-are-running-specific-processes_search-filter"></a>

## Finding deployments that are running specific processes

You can search for deployments that are running a specific process.

| Query                         | Example             |
|-------------------------------|---------------------|
| `Process Name:<process_name>` | `Process Name:bash` |

Search query for finding deployments that run specific processes

<a id="finding-deployments-that-have-serious-but-fixable-vulnerabilities_search-filter"></a>

## Finding deployments that have serious but fixable vulnerabilities

You can search for deployments that have vulnerabilities with a high CVSS score and an available fix.

| Query                         | Example                 |
|-------------------------------|-------------------------|
| `CVSS:<expression_and_score>` | `CVSS:>=6` `Fixable:.*` |

Search query for finding deployments with serious but fixable vulnerabilities

<a id="finding-deployments-that-use-passwords-exposed-through-environment-variables_search-filter"></a>

## Finding deployments that use passwords exposed through environment variables

You can search for deployments that have passwords or credentials exposed through environment variables.

| Query                     | Example                      |
|---------------------------|------------------------------|
| `Environment Key:<query>` | `Environment Key:r/.*pass.*` |

Search query for finding deployments that expose passwords through environment variables

<a id="finding-running-deployments-that-have-particular-software-components-in-them_search-filter"></a>

## Finding running deployments that have particular software components in them

You can search for deployments that contain a specific software component.

| Query                        | Example                                      |
|------------------------------|----------------------------------------------|
| `Component:<component_name>` | `Component:libgpg-error` or `Component:sudo` |

Search query for finding deployments that contain particular software components

<a id="finding-users-or-groups_search-filter"></a>

## Finding users or groups

You can use Kubernetes labels, selectors, and annotations to attach metadata to your deployments and then query based on that metadata to identify individuals or groups.

<div>

<div class="title">

Additional resources

</div>

- [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)

- [Annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)

</div>

<a id="finding-who-owns-a-particular-deployment_search-filter"></a>

## Finding who owns a particular deployment

You can search for the owner of a specific deployment by using labels or annotations.

| Query | Example |
|----|----|
| `Deployment:<deployment_name>` `Label:<key_value>` or `Deployment:<deployment_name>` `Annotation:<key_value>` | `Deployment:app-server` `Label:team=backend` |

Search query for finding the owner of a deployment

<a id="finding-who-is-deploying-images-from-public-registries_search-filter"></a>

## Finding who is deploying images from public registries

You can search for the owner of deployments that use images from public registries by using labels or annotations.

| Query | Example |
|----|----|
| `Image Registry:<registry_name>` `Label:<key_value>` or `Image Registry:<registry_name>` `Annotation:<key_value>` | `Image Registry:docker.io` `Label:team=backend` |

Search query for finding who deploys images from public registries

<a id="finding-who-is-deploying-into-the-default-namespace_search-filter"></a>

## Finding who is deploying into the default namespace

You can search for the owner of deployments in the default namespace by using labels or annotations.

| Query | Example |
|----|----|
| `Namespace:default` `Label:<key_value>` or `Namespace:default` `Annotation:<key_value>` | `Namespace:default` `Label:team=backend` |

Search query for finding who deploys into the default namespace

<a id="search-attributes_search-filter"></a>

# Search attributes

The following table lists the search attributes that you can use while searching and filtering in Red Hat Advanced Cluster Security for Kubernetes.

| Attribute | Description |
|----|----|
| Add Capabilities | Provides the container with additional Linux capabilities, for instance the ability to change files or perform network operations. |
| Annotation | Arbitrary non-identifying metadata attached to an orchestrator object. |
| CPU Cores Limit | Maximum number of cores that a resource can use. |
| CPU Cores Request | Minimum number of cores required for a given resource. |
| CVE | Common Vulnerabilities and Exposures. Use this attribute with specific CVE numbers. |
| CVSS | Common Vulnerability Scoring System. Use this attribute with the CVSS score and the greater than ( \> ), less than ( \< ), or equal to ( = ) symbols. |
| Category | Policy categories include Anomalous Activity, Cryptocurrency Mining, DevOps Best Practices, Docker Center for Internet Security (CIS), File Activity Monitoring, Kubernetes, Kubernetes Events, Network Tools, Package Management, Privileges, Security Best Practices, Supply Chain Security, System Modification, Vulnerability Management, Zero Trust, and any custom policy categories that you create. |
| Cert Expiration | Certificate expiration date. |
| Cluster | Name of a Kubernetes or OpenShift Container Platform cluster. |
| Cluster ID | Unique ID for a Kubernetes or OpenShift Container Platform cluster. |
| Cluster Role | Use `true` to search for cluster-wide roles and `false` for namespace-scoped roles. |
| Component | Software (daemond, docker), objects (images, containers, services), registries (repository for Docker images). |
| Component Count | Number of components in the image. |
| Component version | The version of software, objects, or registries. |
| Created Time | Time and date of secret object creation. |
| Deployment | Name of the deployment. |
| Deployment Type | The type of Kubernetes controller that the deployment uses. |
| Description | Description of the deployment. |
| Dockerfile Instruction Keyword | Keyword in the Dockerfile instructions in an image. |
| Dockerfile Instruction Value | Value in the Dockerfile instructions in an image. |
| Drop Capabilities | Linux capabilities dropped from the container. For example `CAP_SETUID` or `CAP_NET_RAW`. |
| Enforcement | Type of enforcement assigned to the deployment. For example, `None`, `Scale to Zero Replicas`, or `Add an Unsatisfiable Node Constraint`. |
| Environment Key | Key part of a label key-value string that is metadata for further identifying and organizing the environment of a container. |
| Environment Value | Value part of a label key-value string that is metadata for further identifying and organizing the environment of a container. |
| Exposed Node Port | Port number of the exposed node port. |
| Exposing Service | Name of the exposed service. |
| Exposing Service Port | Port number of the exposed service. |
| Exposure Level | The type of exposure for a deployment port, for example `external` or `node`. |
| External Hostname | The hostname for an external port exposure for a deployment. |
| External IP | The IP address for an external port exposure for a deployment. |
| Fixable CVE Count | Number of fixable CVEs on an image. |
| Fixed By | The version string of a package that fixes a flagged vulnerability in an image. |
| Image | The name of the image. |
| Image Command | The command specified in the image. |
| Image Created Time | The time and date of image creation. |
| Image Entrypoint | The entrypoint command specified in the image. |
| Image Pull Secret | The name of the secret to use when pulling the image, as specified in the deployment. |
| Image Pull Secret Registry | The name of the registry for an image pull secret. |
| Image Registry | The name of the image registry. |
| Image Remote | Whether an image is remotely accessible. |
| Image Scan Time | The time and date when the image was last scanned. |
| Image Tag | Identifier for an image. |
| Image Users | Name of the user or group that a container image uses when it runs. |
| Image Volumes | Names of the configured volumes in the container image. |
| Inactive Deployment | Use `true` to search for inactive deployments and `false` for active deployments. |
| Label | The key part of a label key-value string that serves as metadata for further identifying and organizing images, containers, daemons, volumes, networks, and other resources. |
| Lifecycle Stage | The type of lifecycle stage where this policy applies or where an alert triggers. |
| Max Exposure Level | For a deployment, the maximum level of network exposure for all given ports/services. |
| Memory Limit (MB) | Maximum amount of memory that a resource can use. |
| Memory Request (MB) | Minimum amount of memory required for a given resource. |
| Namespace | The name of the namespace. |
| Namespace ID | Unique ID for the containing namespace object on a deployment. |
| Node | Name of a node. |
| Node ID | Unique ID for a node. |
| Pod Label | Single piece of identifying metadata attached to an individual pod. |
| Policy | The name of the security policy. |
| Port | Port numbers exposed by a deployment. |
| Port Protocol | IP protocol, such as Transmission Control Protocol (TCP) or User Datagram Protocol (UDP), that the exposed port uses. |
| Priority | Risk priority for a deployment. This attribute is available only in the **Risks** view. |
| Privileged | Use `true` to search for privileged running deployments, or `false` otherwise. |
| Process Ancestor | Name of any parent process for a process indicator in a deployment. |
| Process Arguments | Command arguments for a process indicator in a deployment. |
| Process Name | Name of the process for a process indicator in a deployment. |
| Process Path | Path to the binary in the container for a process indicator in a deployment. |
| Process UID | Unix user ID for the process indicator in a deployment. |
| Read Only Root Filesystem | Use `true` to search for containers running with the root file system configured as read only. |
| Role | Name of a Kubernetes role-based access control (RBAC) role. |
| Role Binding | Name of a Kubernetes RBAC role binding. |
| Role ID | Role ID that a Kubernetes RBAC role binding references. |
| Secret | Name of the secret object that holds the sensitive information. |
| Secret Path | Path to the secret object in the file system. |
| Secret Type | Type of the secret, for example, certificate or RSA public key. |
| Service Account | Service account name for a service account or deployment. |
| Severity | Level of importance of a violation: Critical, High, Medium, Low. |
| Subject | Name for a subject in Kubernetes RBAC. |
| Subject Kind | Type of subject in Kubernetes RBAC, such as `SERVICE_ACCOUNT`, `USER`, or `GROUP`. |
| Taint Effect | Type of taint currently applied to a node. |
| Taint Key | Key for a taint currently applied to a node. |
| Taint Value | Allowed value for a taint currently applied to a node. |
| Toleration Key | Key for a toleration applied to a deployment. |
| Toleration Value | Value for a toleration applied to a deployment. |
| Violation | A notification displayed on the **Violations** page when a deployment does not meet the conditions that a policy specifies. |
| Violation State | Use it to search for resolved violations. |
| Violation Time | Time and date that a violation first occurred. |
| Volume Destination | Mount path of the data volume. |
| Volume Name | Name of the storage. |
| Volume ReadOnly | Use `true` to search for volumes mounted as read only. |
| Volume Source | The provisioning method for the volume, for example, `persistentVolumeClaim` or `hostPath`. |
| Volume Type | The type of volume. |

Search attributes and their descriptions
