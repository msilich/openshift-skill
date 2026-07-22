<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Understanding the state of the system in Operator Lifecycle Manager (OLM) is important for making decisions about and debugging problems with installed Operators. OLM provides insight into subscriptions and related catalog sources regarding their state and actions performed. This helps users better understand the healthiness of their Operators.

# Operator subscription condition types

Subscriptions can report the following condition types:

| Condition | Description |
|----|----|
| `CatalogSourcesUnhealthy` | Some or all of the catalog sources to be used in resolution are unhealthy. |
| `InstallPlanMissing` | An install plan for a subscription is missing. |
| `InstallPlanPending` | An install plan for a subscription is pending installation. |
| `InstallPlanFailed` | An install plan for a subscription has failed. |
| `ResolutionFailed` | The dependency resolution for a subscription has failed. |

Subscription condition types

> [!NOTE]
> Default OpenShift Container Platform cluster Operators are managed by the Cluster Version Operator (CVO) and they do not have a `Subscription` object. Application Operators are managed by Operator Lifecycle Manager (OLM) and they have a `Subscription` object.

<div>

<div class="title">

Additional resources

</div>

- [Refreshing failing subscriptions](olm-deleting-operators-from-cluster.md#olm-refresh-subs_olm-deleting-operators-from-a-cluster)

</div>

# Viewing Operator subscription status by using the CLI

You can view Operator subscription status by using the CLI.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  List Operator subscriptions:

    ``` terminal
    $ oc get subs -n <operator_namespace>
    ```

2.  Use the `oc describe` command to inspect a `Subscription` resource:

    ``` terminal
    $ oc describe sub <subscription_name> -n <operator_namespace>
    ```

3.  In the command output, find the `Conditions` section for the status of Operator subscription condition types. In the following example, the `CatalogSourcesUnhealthy` condition type has a status of `false` because all available catalog sources are healthy:

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Name:         cluster-logging
    Namespace:    openshift-logging
    Labels:       operators.coreos.com/cluster-logging.openshift-logging=
    Annotations:  <none>
    API Version:  operators.coreos.com/v1alpha1
    Kind:         Subscription
    # ...
    Conditions:
       Last Transition Time:  2019-07-29T13:42:57Z
       Message:               all available catalogsources are healthy
       Reason:                AllCatalogSourcesHealthy
       Status:                False
       Type:                  CatalogSourcesUnhealthy
    # ...
    ```

    </div>

</div>

> [!NOTE]
> Default OpenShift Container Platform cluster Operators are managed by the Cluster Version Operator (CVO) and they do not have a `Subscription` object. Application Operators are managed by Operator Lifecycle Manager (OLM) and they have a `Subscription` object.

# Viewing Operator catalog source status by using the CLI

You can view the status of an Operator catalog source by using the CLI.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  List the catalog sources in a namespace. For example, you can check the `openshift-marketplace` namespace, which is used for cluster-wide catalog sources:

    ``` terminal
    $ oc get catalogsources -n openshift-marketplace
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                  DISPLAY               TYPE   PUBLISHER   AGE
    certified-operators   Certified Operators   grpc   Red Hat     55m
    community-operators   Community Operators   grpc   Red Hat     55m
    example-catalog       Example Catalog       grpc   Example Org 2m25s
    redhat-operators      Red Hat Operators     grpc   Red Hat     55m
    ```

    </div>

2.  Use the `oc describe` command to get more details and status about a catalog source:

    ``` terminal
    $ oc describe catalogsource example-catalog -n openshift-marketplace
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Name:         example-catalog
    Namespace:    openshift-marketplace
    Labels:       <none>
    Annotations:  operatorframework.io/managed-by: marketplace-operator
                  target.workload.openshift.io/management: {"effect": "PreferredDuringScheduling"}
    API Version:  operators.coreos.com/v1alpha1
    Kind:         CatalogSource
    # ...
    Status:
      Connection State:
        Address:              example-catalog.openshift-marketplace.svc:50051
        Last Connect:         2021-09-09T17:07:35Z
        Last Observed State:  TRANSIENT_FAILURE
      Registry Service:
        Created At:         2021-09-09T17:05:45Z
        Port:               50051
        Protocol:           grpc
        Service Name:       example-catalog
        Service Namespace:  openshift-marketplace
    # ...
    ```

    </div>

    In the preceding example output, the last observed state is `TRANSIENT_FAILURE`. This state indicates that there is a problem establishing a connection for the catalog source.

3.  List the pods in the namespace where your catalog source was created:

    ``` terminal
    $ oc get pods -n openshift-marketplace
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                    READY   STATUS             RESTARTS   AGE
    certified-operators-cv9nn               1/1     Running            0          36m
    community-operators-6v8lp               1/1     Running            0          36m
    marketplace-operator-86bfc75f9b-jkgbc   1/1     Running            0          42m
    example-catalog-bwt8z                   0/1     ImagePullBackOff   0          3m55s
    redhat-operators-smxx8                  1/1     Running            0          36m
    ```

    </div>

    When a catalog source is created in a namespace, a pod for the catalog source is created in that namespace. In the preceding example output, the status for the `example-catalog-bwt8z` pod is `ImagePullBackOff`. This status indicates that there is an issue pulling the catalog source’s index image.

4.  Use the `oc describe` command to inspect a pod for more detailed information:

    ``` terminal
    $ oc describe pod example-catalog-bwt8z -n openshift-marketplace
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Name:         example-catalog-bwt8z
    Namespace:    openshift-marketplace
    Priority:     0
    Node:         ci-ln-jyryyg2-f76d1-ggdbq-worker-b-vsxjd/10.0.128.2
    ...
    Events:
      Type     Reason          Age                From               Message
      ----     ------          ----               ----               -------
      Normal   Scheduled       48s                default-scheduler  Successfully assigned openshift-marketplace/example-catalog-bwt8z to ci-ln-jyryyf2-f76d1-fgdbq-worker-b-vsxjd
      Normal   AddedInterface  47s                multus             Add eth0 [10.131.0.40/23] from openshift-sdn
      Normal   BackOff         20s (x2 over 46s)  kubelet            Back-off pulling image "quay.io/example-org/example-catalog:v1"
      Warning  Failed          20s (x2 over 46s)  kubelet            Error: ImagePullBackOff
      Normal   Pulling         8s (x3 over 47s)   kubelet            Pulling image "quay.io/example-org/example-catalog:v1"
      Warning  Failed          8s (x3 over 47s)   kubelet            Failed to pull image "quay.io/example-org/example-catalog:v1": rpc error: code = Unknown desc = reading manifest v1 in quay.io/example-org/example-catalog: unauthorized: access to the requested resource is not authorized
      Warning  Failed          8s (x3 over 47s)   kubelet            Error: ErrImagePull
    ```

    </div>

    In the preceding example output, the error messages indicate that the catalog source’s index image is failing to pull successfully because of an authorization issue. For example, the index image might be stored in a registry that requires login credentials.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Operator Lifecycle Manager concepts and resources → Catalog source](../understanding/olm/olm-understanding-olm.md#olm-catalogsource_olm-understanding-olm)

- gRPC documentation: [States of Connectivity](https://grpc.github.io/grpc/core/md_doc_connectivity-semantics-and-api.html)

- [Accessing images for Operators from private registries](olm-managing-custom-catalogs.md#olm-accessing-images-private-registries_olm-managing-custom-catalogs)

</div>
