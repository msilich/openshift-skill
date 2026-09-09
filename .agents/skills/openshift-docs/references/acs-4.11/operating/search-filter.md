<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The ability to instantly find resources is important to safeguard your cluster. Use Red Hat Advanced Cluster Security for Kubernetes search feature to find relevant resources faster. For example, you can use it to find deployments that are exposed to a newly published CVE or find all deployments that have external network exposure.

<a id="search-syntax_search-filter"></a>

# Search syntax

A search query is made up of two parts:

- An attribute that identifies the resource type you want to search for.

- A search term that finds the matching resource.

For example, to find all violations in the `visa-processor` deployment, the search query is `Deployment:visa-processor`. In this search query, `Deployment` is the attribute and `visa-processor` is the search term.

> [!NOTE]
> You must select an attribute before you can use search terms. However, in some views, such as the **Risk** view and the **Violations** view, Red Hat Advanced Cluster Security for Kubernetes automatically applies the relevant attribute based on the search term you enter.

- You can use multiple attributes in your query. When you use more than one attribute, the results only include the items that match all attributes.

  <div class="formalpara">

  <div class="title">

  Example

  </div>

  When you search for `Namespace:frontend CVE:CVE-2018-11776`, it returns only those resources which violate CVE-2018-11776 in the `frontend` namespace.

  </div>

- You can use more than one search term with each attribute. When you use more than one search term, the results include all items that match any of the search terms.

  <div class="formalpara">

  <div class="title">

  Example

  </div>

  If you use the search query `Namespace: frontend backend`, it returns matching results from the namespace `frontend` or `backend`.

  </div>

- You can combine multiple attribute and search term pairs.

  <div class="formalpara">

  <div class="title">

  Example

  </div>

  The search query `Cluster:production Namespace:frontend CVE:CVE-2018-11776` returns all resources which violate CVE-2018-11776 in the `frontend` namespace in the `production` cluster.

  </div>

- Search terms can be part of a word, in which case Red Hat Advanced Cluster Security for Kubernetes returns all matching results.

  <div class="formalpara">

  <div class="title">

  Example

  </div>

  If you search for `Deployment:def`, the results include all deployments starting with `def`.

  </div>

- To explicitly search for a specific term, use the search terms inside quotes.

  <div class="formalpara">

  <div class="title">

  Example

  </div>

  When you search for `Deployment:"def"`, the results only include the deployment `def`.

  </div>

- You can also use regular expressions by using `r/` before your search term.

  <div class="formalpara">

  <div class="title">

  Example

  </div>

  When you search for `Namespace:r/st.*x`, the results include matches from namespace `stackrox` and `stix`.

  </div>

- Use `!` to indicate the search terms that you do not want in results.

  <div class="formalpara">

  <div class="title">

  Example

  </div>

  If you search for `Namespace:!stackrox`, the results include matches from all namespaces except the `stackrox` namespace.

  </div>

- Use the comparison operators `>`, `<`, `=`, `>=`, or `<=` to match a specific value or range of values.

  <div class="formalpara">

  <div class="title">

  Example

  </div>

  If you search for `CVSS:>=6`, the results include all vulnerabilities with Common Vulnerability Scoring System (CVSS) score 6 or higher.

  </div>

<a id="search-autocomplete_search-filter"></a>

# Search autocomplete

As you enter your query, Red Hat Advanced Cluster Security for Kubernetes automatically displays relevant suggestions for the attributes and the search terms.

<a id="use-global-search_search-filter"></a>

# Using global search

By using global search you can search across all resources in your environment. Based on the resource type you use in your search query, the results are grouped in the following categories:

- All results (Lists matching results across all categories)

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

These categories are listed as a table on the RHACS portal global search page and you can click on the category name to identify results belonging to the selected category.

To do a global search, in the RHACS portal, select **Search**.

<a id="use-local-page-filtering_search-filter"></a>

# Using local page filtering

You can use local page filtering from within all views in the RHACS portal. Local page filtering works similar to the global search, but only relevant attributes are available. You can select the search bar to show all available attributes for a specific view.

<a id="common-search-queries_search-filter"></a>

# Common search queries

Here are some common search queries you can run with Red Hat Advanced Cluster Security for Kubernetes.

<a id="_finding_deployments_that_are_affected_by_a_specific_cve"></a>

## Finding deployments that are affected by a specific CVE

| Query              | Example              |
|--------------------|----------------------|
| `CVE:<CVE_number>` | `CVE:CVE-2018-11776` |

<a id="_finding_privileged_running_deployments"></a>

## Finding privileged running deployments

| Query                        | Example           |
|------------------------------|-------------------|
| `Privileged:<true_or_false>` | `Privileged:true` |

<a id="_finding_deployments_that_have_external_network_exposure"></a>

## Finding deployments that have external network exposure

| Query                    | Example                   |
|--------------------------|---------------------------|
| `Exposure Level:<level>` | `Exposure Level:External` |

<a id="_finding_deployments_that_are_running_specific_processes"></a>

## Finding deployments that are running specific processes

| Query                         | Example             |
|-------------------------------|---------------------|
| `Process Name:<process_name>` | `Process Name:bash` |

<a id="_finding_deployments_that_have_serious_but_fixable_vulnerabilities"></a>

## Finding deployments that have serious but fixable vulnerabilities

| Query                         | Example                 |
|-------------------------------|-------------------------|
| `CVSS:<expression_and_score>` | `CVSS:>=6` `Fixable:.*` |

<a id="_finding_deployments_that_use_passwords_exposed_through_environment_variables"></a>

## Finding deployments that use passwords exposed through environment variables

| Query                     | Example                      |
|---------------------------|------------------------------|
| `Environment Key:<query>` | `Environment Key:r/.*pass.*` |

<a id="_finding_running_deployments_that_have_particular_software_components_in_them"></a>

## Finding running deployments that have particular software components in them

| Query                        | Example                                      |
|------------------------------|----------------------------------------------|
| `Component:<component_name>` | `Component:libgpg-error` or `Component:sudo` |

<a id="_finding_users_or_groups"></a>

## Finding users or groups

Use Kubernetes [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/), and [Annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) to attach metadata to your deployments. You can then query based on the applied annotations and labels to identify individuals or groups.

<a id="_finding_who_owns_a_particular_deployment"></a>

### Finding who owns a particular deployment

| Query | Example |
|----|----|
| `Deployment:<deployment_name>` `Label:<key_value>` or `Deployment:<deployment_name>` `Annotation:<key_value>` | `Deployment:app-server` `Label:team=backend` |

<a id="_finding_who_is_deploying_images_from_public_registries"></a>

### Finding who is deploying images from public registries

| Query | Example |
|----|----|
| `Image Registry:<registry_name>` `Label:<key_value>` or `Image Registry:<registry_name>` `Annotation:<key_value>` | `Image Registry:docker.io` `Label:team=backend` |

<a id="_finding_who_is_deploying_into_the_default_namespace"></a>

### Finding who is deploying into the default namespace

| Query | Example |
|----|----|
| `Namespace:default` `Label:<key_value>` or `Namespace:default` `Annotation:<key_value>` | `Namespace:default` `Label:team=backend` |

<a id="search-attributes_search-filter"></a>

# Search attributes

Following is the list of search attributes that you can use while searching and filtering in Red Hat Advanced Cluster Security for Kubernetes.

| **Attribute** | **Description** |
|----|----|
| Add Capabilities | Provides the container with additional Linux capabilities, for instance the ability to modify files or perform network operations. |
| Annotation | Arbitrary non-identifying metadata attached to an orchestrator object. |
| CPU Cores Limit | Maximum number of cores that a resource is allowed to use. |
| CPU Cores Request | Minimum number of cores to be reserved for a given resource. |
| CVE | Common Vulnerabilities and Exposures, use it with specific CVE numbers. |
| CVSS | Common Vulnerability Scoring System, use it with the CVSS score and greater than ( \> ), less than ( \< ), or equal to ( = ) symbols. |
| Category | Policy categories include Anomalous Activity, Cryptocurrency Mining, DevOps Best Practices, Docker Center for Internet Security (CIS), File Activity Monitoring, Kubernetes, Kubernetes Events, Network Tools, Package Management, Privileges, Security Best Practices, Supply Chain Security, System Modification, Vulnerability Management, Zero Trust, and any custom policy categories that you create. |
| Cert Expiration | Certificate expiration date. |
| Cluster | Name of a Kubernetes or OpenShift Container Platform cluster. |
| Cluster ID | Unique ID for a Kubernetes or OpenShift Container Platform cluster. |
| Cluster Role | Use `true` to search for cluster-wide roles and `false` for namespace-scoped roles. |
| Component | Software (daemond, docker), objects (images, containers, services), registries (repository for Docker images). |
| Component Count | Number of components in the image. |
| Component version | The version of software, objects, or registries. |
| Created Time | Time and date when the secret object was created. |
| Deployment | Name of the deployment. |
| Deployment Type | The type of Kubernetes controller on which the deployment is based. |
| Description | Description of the deployment. |
| Dockerfile Instruction Keyword | Keyword in the Dockerfile instructions in an image. |
| Dockerfile Instruction Value | Value in the Dockerfile instructions in an image. |
| Drop Capabilities | Linux capabilities that have been dropped from the container. For example `CAP_SETUID` or `CAP_NET_RAW`. |
| Enforcement | Type of enforcement assigned to the deployment. For example, `None`, `Scale to Zero Replicas`, or `Add an Unsatisfiable Node Constraint`. |
| Environment Key | Key portion of a label key-value string that is metadata for further identifying and organizing the environment of a container. |
| Environment Value | Value portion of a label key-value string that is metadata for further identifying and organizing the environment of a container. |
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
| Image Created Time | The time and date when the image was created. |
| Image Entrypoint | The entrypoint command specified in the image. |
| Image Pull Secret | The name of the secret to use when pulling the image, as specified in the deployment. |
| Image Pull Secret Registry | The name of the registry for an image pull secret. |
| Image Registry | The name of the image registry. |
| Image Remote | Indication of an image that is remotely accessible. |
| Image Scan Time | The time and date when the image was last scanned. |
| Image Tag | Identifier for an image. |
| Image Users | Name of the user or group that a container image is configured to use when it runs. |
| Image Volumes | Names of the configured volumes in the container image. |
| Inactive Deployment | Use `true` to search for inactive deployments and `false` for active deployments. |
| Label | The key portion of a label key-value string that is metadata for further identifying and organizing images, containers, daemons, volumes, networks, and other resources. |
| Lifecycle Stage | The type of lifecycle stage where this policy is configured or alert was triggered. |
| Max Exposure Level | For a deployment, the maximum level of network exposure for all given ports/services. |
| Memory Limit (MB) | Maximum amount of memory that a resource is allowed to use. |
| Memory Request (MB) | Minimum amount of memory to be reserved for a given resource. |
| Namespace | The name of the namespace. |
| Namespace ID | Unique ID for the containing namespace object on a deployment. |
| Node | Name of a node. |
| Node ID | Unique ID for a node. |
| Pod Label | Single piece of identifying metadata attached to an individual pod. |
| Policy | The name of the security policy. |
| Port | Port numbers exposed by a deployment. |
| Port Protocol | IP protocol such as TCP or UDP used by exposed port. |
| Priority | Risk priority for a deployment. (Only available in **Risks** view.) |
| Privileged | Use `true` to search for privileged running deployments, or `false` otherwise. |
| Process Ancestor | Name of any parent process for a process indicator in a deployment. |
| Process Arguments | Command arguments for a process indicator in a deployment. |
| Process Name | Name of the process for a process indicator in a deployment. |
| Process Path | Path to the binary in the container for a process indicator in a deployment. |
| Process UID | Unix user ID for the process indicator in a deployment. |
| Read Only Root Filesystem | Use `true` to search for containers running with the root file system configured as read only. |
| Role | Name of a Kubernetes RBAC role. |
| Role Binding | Name of a Kubernetes RBAC role binding. |
| Role ID | Role ID to which a Kubernetes RBAC role binding is bound. |
| Secret | Name of the secret object that holds the sensitive information. |
| Secret Path | Path to the secret object in the file system. |
| Secret Type | Type of the secret, for example, certificate or RSA public key. |
| Service Account | Service account name for a service account or deployment. |
| Severity | Indication of level of importance of a violation: Critical, High, Medium, Low. |
| Subject | Name for a subject in Kubernetes RBAC. |
| Subject Kind | Type of subject in Kubernetes RBAC, such as `SERVICE_ACCOUNT`, `USER` or `GROUP`. |
| Taint Effect | Type of taint currently applied to a node. |
| Taint Key | Key for a taint currently applied to a node. |
| Taint Value | Allowed value for a taint currently applied to a node. |
| Toleration Key | Key for a toleration applied to a deployment. |
| Toleration Value | Value for a toleration applied to a deployment. |
| Violation | A notification displayed in the **Violations** page when the conditions specified by a policy have not been met. |
| Violation State | Use it to search for resolved violations. |
| Violation Time | Time and date that a violation first occurred. |
| Volume Destination | Mount path of the data volume. |
| Volume Name | Name of the storage. |
| Volume ReadOnly | Use `true` to search for volumes that are mounted as read only. |
| Volume Source | Indicates the form in which the volume is provisioned (for example, `persistentVolumeClaim` or `hostPath`). |
| Volume Type | The type of volume. |
