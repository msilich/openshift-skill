<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

A multi-project quota, defined by a `ClusterResourceQuota` object, shares quotas across multiple projects. The system aggregates the resources used in each selected project and applies the aggregate limit across all selected projects.

This guide describes how cluster administrators can set and manage resource quotas across multiple projects.

> [!IMPORTANT]
> Do not run workloads in or share access to default projects. Default projects are reserved for running core cluster components.
>
> The following default projects are considered highly privileged: `default`, `kube-public`, `kube-system`, `openshift`, `openshift-infra`, `openshift-node`, and other system-created projects that have the `openshift.io/run-level` label set to `0` or `1`. Functionality that relies on admission plugins, such as pod security admission, security context constraints, cluster resource quotas, and image reference resolution, does not work in highly privileged projects.

# Selecting multiple projects during quota creation

To aggregate resource usage and enforce consistent limits across multiple namespaces, you can select target projects by using annotation or label selectors when creating a `ClusterResourceQuota` object.

<div>

<div class="title">

Procedure

</div>

1.  To select projects based on annotations, run the following command:

    ``` terminal
    $ oc create clusterquota for-user \
         --project-annotation-selector openshift.io/requester=<user_name> \
         --hard pods=10 \
         --hard secrets=20
    ```

    This creates the following `ClusterResourceQuota` object:

    ``` yaml
    apiVersion: quota.openshift.io/v1
    kind: ClusterResourceQuota
    metadata:
      name: for-user
    spec:
      quota:
        hard:
          pods: "10"
          secrets: "20"
      selector:
        annotations:
          openshift.io/requester: <user_name>
        labels: null
    status:
      namespaces:
      - namespace: ns-one
        status:
          hard:
            pods: "10"
            secrets: "20"
          used:
            pods: "1"
            secrets: "9"
      total:
        hard:
          pods: "10"
          secrets: "20"
        used:
          pods: "1"
          secrets: "9"
    ```

    where:

    `spec.quota`
    The `ResourceQuotaSpec` object that will be enforced over the selected projects.

    `spec.selector.annotations`
    A simple key-value selector for annotations.

    `spec.selector.labels`
    A label selector that can be used to select projects.

    `status.namespaces`
    A per-namespace map that describes current quota usage in each selected project.

    `status.total`
    The aggregate usage across all selected projects.

    This multi-project quota document controls all projects requested by `<user_name>` using the default project request endpoint. You are limited to 10 pods and 20 secrets.

2.  Similarly, to select projects based on labels, run this command:

    ``` terminal
    $  oc create clusterresourcequota for-name \
        --project-label-selector=name=frontend \
        --hard=pods=10 --hard=secrets=20
    ```

    where:

    `clusterresourcequota`
    Both `clusterresourcequota` and `clusterquota` are aliases of the same command. `for-name` is the name of the `ClusterResourceQuota` object.

    `--project-label-selector`
    To select projects by label, provide a key-value pair by using the format `--project-label-selector=key=value`.

    This creates the following `ClusterResourceQuota` object definition:

    ``` yaml
    apiVersion: quota.openshift.io/v1
    kind: ClusterResourceQuota
    metadata:
      creationTimestamp: null
      name: for-name
    spec:
      quota:
        hard:
          pods: "10"
          secrets: "20"
      selector:
        annotations: null
        labels:
          matchLabels:
            name: frontend
    ```

</div>

# Viewing applicable cluster resource quotas

View the multi-project quota documents applied to your project by using the `AppliedClusterResourceQuota` resource. Although, as an administrator, you cannot create or modify multi-project quotas, you can monitor your project’s resource limits.

<div>

<div class="title">

Procedure

</div>

- To view quotas applied to a project, run:

  ``` terminal
  $ oc describe AppliedClusterResourceQuota
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  Name:   for-user
  Namespace:  <none>
  Created:  19 hours ago
  Labels:   <none>
  Annotations:  <none>
  Label Selector: <null>
  AnnotationSelector: map[openshift.io/requester:<user-name>]
  Resource  Used  Hard
  --------  ----  ----
  pods        1     10
  secrets     9     20
  ```

  </div>

</div>

# Selection granularity

When you create a multi-project quota, restrict the number of active projects to avoid degrading API server responsiveness.

When you configure a multi-project quota using a `ClusterResourceQuota` object, restrict the number of selected active projects to 100 or fewer. Because quota allocation claims require system locking, selecting more than 100 projects under a single multi-project quota can severely degrade API server responsiveness across those projects.
