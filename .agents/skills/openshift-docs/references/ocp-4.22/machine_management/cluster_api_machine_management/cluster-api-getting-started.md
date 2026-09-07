<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The Machine API and Cluster API are distinct API groups that have similar resources. You can use these API groups to automate the management of infrastructure resources on your OpenShift Container Platform cluster.

> [!IMPORTANT]
> Managing machines with the Cluster API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

When you install a standard OpenShift Container Platform cluster that has three control plane nodes, three compute nodes, and uses the default configuration options, the installation program provisions the following infrastructure resources in the `openshift-machine-api` namespace

- One control plane machine set that manages three control plane machines.

- One or more compute machine sets that manage three compute machines.

- One machine health check that manages spot instances.

When you install a cluster that supports managing infrastructure resources with the Cluster API, the installation program provisions the following resources in the `openshift-cluster-api` namespace:

- One cluster resource.

- One provider-specific infrastructure cluster resource.

On clusters that support migrating Machine API resources to Cluster API resources, a two-way synchronization controller creates these primary resources automatically. For more information, see "Machine API to Cluster API resource migration".

# Creating the Cluster API primary resources

For clusters that do not support migrating Machine API resources to Cluster API resources, you must manually create the following Cluster API resources in the `openshift-cluster-api` namespace:

- One or more machine templates that correspond to compute machine sets.

- One or more compute machine sets that manage three compute machines.

## Creating a Cluster API machine template

You can create a provider-specific machine template resource by creating a YAML manifest file and applying it with the OpenShift CLI (`oc`).

<div>

<div class="title">

Prerequisites

</div>

- You have deployed an OpenShift Container Platform cluster.

- You have enabled the use of the Cluster API.

- You have access to the cluster using an account with `cluster-admin` permissions.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file similar to the following example. This procedure uses `<machine_template_resource_file>.yaml` as an example file name.

    ``` yaml
    apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
    kind: <machine_template_kind>
    metadata:
      name: <template_name>
      namespace: openshift-cluster-api
    spec:
      template:
        spec:
    ```

    where:

    `kind`
    Specifies the machine template kind. This value must match the value for your platform.

    The following values are valid:

    | Cluster infrastructure provider    | Value                      |
    |------------------------------------|----------------------------|
    | Amazon Web Services (AWS)          | `AWSMachineTemplate`       |
    | Google Cloud                       | `GCPMachineTemplate`       |
    | Microsoft Azure                    | `AzureMachineTemplate`     |
    | Red Hat OpenStack Platform (RHOSP) | `OpenStackMachineTemplate` |
    | VMware vSphere                     | `VSphereMachineTemplate`   |
    | Bare metal                         | `Metal3MachineTemplate`    |

    `metadata.name`
    Specifies a name for the machine template.

    `spec.template.spec`
    Specifies the details for your environment. These parameters are provider specific. For more information, see the sample Cluster API machine template YAML for your provider.

2.  Create the machine template CR by running the following command:

    ``` terminal
    $ oc create -f <machine_template_resource_file>.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Confirm that the machine template CR is created by running the following command:

  ``` terminal
  $ oc get <machine_template_kind> -n openshift-cluster-api
  ```

  Replace `<machine_template_kind>` with the value that corresponds to your platform.

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` text
  NAME              AGE
  <template_name>   77m
  ```

  </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Machine API to Cluster API resource migration](cluster-api-getting-started.md#mapi-to-capi-migration-overview_cluster-api-getting-started)

- [Sample YAML for a Cluster API machine template resource on Amazon Web Services](cluster_api_provider_configurations/cluster-api-config-options-aws.md#capi-yaml-machine-template-aws_cluster-api-config-options-aws)

- [Sample YAML for a Cluster API machine template resource on Google Cloud](cluster_api_provider_configurations/cluster-api-config-options-gcp.md#capi-yaml-machine-template-gcp_cluster-api-config-options-gcp)

- [Sample YAML for a Cluster API machine template resource on Microsoft Azure](cluster_api_provider_configurations/cluster-api-config-options-azure.md#capi-yaml-machine-template-azure_cluster-api-config-options-azure)

- [Sample YAML for a Cluster API machine template resource on RHOSP](cluster_api_provider_configurations/cluster-api-config-options-rhosp.md#capi-yaml-machine-template-rhosp_cluster-api-config-options-rhosp)

- [Sample YAML for a Cluster API machine template resource on VMware vSphere](cluster_api_provider_configurations/cluster-api-config-options-vsphere.md#capi-yaml-machine-template-vsphere_cluster-api-config-options-vsphere)

- [Sample YAML for a Cluster API machine template resource on bare metal](cluster_api_provider_configurations/cluster-api-config-options-bare-metal.md#capi-yaml-machine-template-bare-metal_cluster-api-config-options-bare-metal)

</div>

## Creating a Cluster API compute machine set

You can create compute machine sets that use the Cluster API to dynamically manage the machine compute resources for specific workloads of your choice.

<div>

<div class="title">

Prerequisites

</div>

- You have deployed an OpenShift Container Platform cluster.

- You have enabled the use of the Cluster API.

- You have access to the cluster using an account with `cluster-admin` permissions.

- You have installed the OpenShift CLI (`oc`).

- You have created the machine template resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file similar to the following. This procedure uses `<machine_set_resource_file>.yaml` as an example file name.

    ``` yaml
    apiVersion: cluster.x-k8s.io/v1beta1
    kind: MachineSet
    metadata:
      name: <machine_set_name>
      namespace: openshift-cluster-api
    spec:
      clusterName: <cluster_name>
      replicas: 1
      selector:
        matchLabels:
          test: example
      template:
        metadata:
          labels:
            test: example
        spec:
    # ...
    ```

    where:

    `metadata.name`
    Specifies a name for the compute machine set. The cluster ID, machine role, and region form a typical pattern for this value in the following format: `<cluster_name>-<role>-<region>`.

    `spec.clusterName`
    Specifies the name of the cluster. Obtain the value of the cluster ID by running the following command:

    ``` terminal
    $  oc get infrastructure cluster \
       -o jsonpath='{.status.infrastructureName}'
    ```

    `spec.template.spec`
    Specifies the details for your environment. These parameters are provider specific. For more information, see the sample Cluster API compute machine set YAML for your provider.

2.  Create the compute machine set CR by running the following command:

    ``` terminal
    $ oc create -f <machine_set_resource_file>.yaml
    ```

3.  Confirm that the compute machine set CR is created by running the following command:

    ``` terminal
    $ oc get machineset.cluster.x-k8s.io -n openshift-cluster-api
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` text
    NAME                 CLUSTER          REPLICAS   READY   AVAILABLE   AGE   VERSION
    <machine_set_name>   <cluster_name>   1          1       1           17m
    ```

    </div>

    When the new compute machine set is available, the `REPLICAS` and `AVAILABLE` values match. If the compute machine set is not available, wait a few minutes and run the command again.

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the compute machine set is creating machines according to your required configuration, review the lists of machines and nodes in the cluster by running the following commands:

  - View the list of Cluster API machines:

    ``` terminal
    $ oc get machine.cluster.x-k8s.io -n openshift-cluster-api
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` text
    NAME                             CLUSTER          NODENAME                                 PROVIDERID      PHASE     AGE     VERSION
    <machine_set_name>-<string_id>   <cluster_name>   <ip_address>.<region>.compute.internal   <provider_id>   Running   8m23s
    ```

    </div>

  - View the list of nodes:

    ``` terminal
    $ oc get node
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` text
    NAME                                       STATUS   ROLES    AGE     VERSION
    <ip_address_1>.<region>.compute.internal   Ready    worker   5h14m   v1.28.5
    <ip_address_2>.<region>.compute.internal   Ready    master   5h19m   v1.28.5
    <ip_address_3>.<region>.compute.internal   Ready    worker   7m      v1.28.5
    ```

    </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Sample YAML for a Cluster API compute machine set resource on Amazon Web Services](cluster_api_provider_configurations/cluster-api-config-options-aws.md#capi-yaml-machine-set-aws_cluster-api-config-options-aws)

- [Sample YAML for a Cluster API compute machine set resource on Google Cloud](cluster_api_provider_configurations/cluster-api-config-options-gcp.md#capi-yaml-machine-set-gcp_cluster-api-config-options-gcp)

- [Sample YAML for a Cluster API compute machine set resource on Microsoft Azure](cluster_api_provider_configurations/cluster-api-config-options-azure.md#capi-yaml-machine-set-azure_cluster-api-config-options-azure)

- [Sample YAML for a Cluster API compute machine set resource on RHOSP](cluster_api_provider_configurations/cluster-api-config-options-rhosp.md#capi-yaml-machine-set-rhosp_cluster-api-config-options-rhosp)

- [Sample YAML for a Cluster API compute machine set resource on VMware vSphere](cluster_api_provider_configurations/cluster-api-config-options-vsphere.md#capi-yaml-machine-set-vsphere_cluster-api-config-options-vsphere)

- [Sample YAML for a Cluster API compute machine set resource on bare metal](cluster_api_provider_configurations/cluster-api-config-options-bare-metal.md#capi-yaml-machine-set-bare-metal_cluster-api-config-options-bare-metal)

</div>

# Machine API to Cluster API resource migration

On clusters that support migrating Machine API resources to Cluster API resources, a two-way synchronization controller creates the Cluster API resources in the `openshift-cluster-api` namespace.

These Cluster API resources are listed as follows:

- One or more machine templates that correspond to compute machine sets.

- One or more compute machine sets that manage three compute machines.

- One or more Cluster API compute machines that correspond to each Machine API compute machine.

> [!NOTE]
> The two-way synchronization controller only operates on clusters with the `MachineAPIMigration` feature gate in the `TechPreviewNoUpgrade` feature set enabled.

These Cluster API resources correspond to the resources that the installation program provisions in the `openshift-machine-api` namespace for a cluster that uses the default configuration options. The Cluster API resources have the same names as their Machine API counterparts and appear in the output of commands, such as `oc get`, that list resources. The synchronization controller creates the Cluster API resources in an unprovisioned (`Paused`) state to prevent unintended reconciliation.

For supported configurations, you can migrate a Machine API resource to the equivalent Cluster API resource by changing which API it considers authoritative. When you migrate a Machine API resources to the Cluster API, you transfer management of the resource to the Cluster API.

By migrating a Machine API resource to use the Cluster API, you can verify that everything works as expected before deciding to use the Cluster API in production clusters. After migrating a Machine API resource to an equivalent Cluster API resource, you can examine the new resource to verify that the features and configuration match the original Machine API resource.

When you change the authoritative API for a compute machine set, any existing compute machines that the compute machine set manages retain their original authoritative API. As a result, a compute machine set that manages machines that use different authoritative APIs is a valid and expected occurrence in clusters that support migrating between these API types.

When you change the authoritative API for a compute machine, the instance on the underlying infrastructure that backs the machine is not recreated or reprovisioned. In-place changes, such as modifying labels, tags, taints, or annotations, are the only changes that the API group can make to the underlying instance that backs the machine.

> [!NOTE]
> You can only migrate some resources on supported infrastructure types.

| Infrastructure | Compute machine | Compute machine set | Machine health check | Control plane machine set | Cluster autoscaler |
|----|----|----|----|----|----|
| AWS | Technology Preview | Technology Preview | Not Available | Not Available | Not Available |
| All other infrastructure types | Not Available | Not Available | Not Available | Not Available | Not Available |

Supported resource conversions

## Authoritative API types of compute machines

The values of the `.spec.authoritativeAPI` and `.spec.template.spec.authoritativeAPI` fields in a Machine API compute machine set determine the authoritative API of the compute machines.

|  |  |  |  |  |
|----|----|----|----|----|
| **`.spec.authoritativeAPI` value** | `ClusterAPI` | `ClusterAPI` | `MachineAPI` | `MachineAPI` |
| **`.spec.template.spec.authoritativeAPI` value** | `ClusterAPI` | `MachineAPI` | `MachineAPI` | `ClusterAPI` |
| **`authoritativeAPI` value for new compute machines** | `ClusterAPI` | `ClusterAPI` | `MachineAPI` | `ClusterAPI` |

Interaction of `authoritativeAPI` fields when creating compute machines

> [!NOTE]
> When the `.spec.authoritativeAPI` value is `ClusterAPI`, the Machine API machine set is not authoritative and the `.spec.template.spec.authoritativeAPI` value is not used. As a result, the only combination that creates a compute machine with the Machine API as authoritative is where the `.spec.authoritativeAPI` and `.spec.template.spec.authoritativeAPI` values are `MachineAPI`.

## Migrating a Machine API resource to use the Cluster API

You can migrate individual Machine API objects to equivalent Cluster API objects.

> [!IMPORTANT]
> Migrating a Machine API resource to use the Cluster API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Prerequisites

</div>

- You have deployed an OpenShift Container Platform cluster on a supported infrastructure type.

- You have enabled the use of the Cluster API.

- You have enabled the `MachineAPIMigration` feature gate in the `TechPreviewNoUpgrade` feature set.

- You have access to the cluster using an account with `cluster-admin` permissions.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Identify the Machine API resource that you want to migrate to a Cluster API resource by running the following command:

    ``` terminal
    $ oc get <resource_kind> -n openshift-machine-api
    ```

    where `<resource_kind>` is one of the following values:

    `machine.machine.openshift.io`
    The fully qualified name of the resource kind for a compute or control plane machine.

    `machineset.machine.openshift.io`
    The fully qualified name of the resource kind for a compute machine set.

2.  Edit the resource specification by running the following command:

    ``` terminal
    $ oc edit <resource_kind>/<resource_name> -n openshift-machine-api
    ```

    where:

    `<resource_kind>`
    Specifies a compute machine with `machine.machine.openshift.io` or compute machine set with `machineset.machine.openshift.io`.

    `<resource_name>`
    Specifies the name of the Machine API resource that you want to migrate to a Cluster API resource.

3.  In the resource specification, update the value of the `spec.authoritativeAPI` field:

    ``` yaml
    apiVersion: machine.openshift.io/v1beta1
    kind: <resource_kind>
    metadata:
      name: <resource_name>
      [...]
    spec:
      authoritativeAPI: ClusterAPI
      [...]
    status:
      authoritativeAPI: MachineAPI
      [...]
    ```

    where:

    `kind`
    Specifies the resource kind of the resource that you want to migrate. For example, the resource kind for a compute machine set is `MachineSet` and the resource kind for a compute machine is `Machine`.

    `metadata.name`
    Specifies the name of the resource that you want to migrate.

    `spec.authoritativeAPI`
    Specifies the authoritative API that you want this resource to use. For example, to start migrating a Machine API resource to the Cluster API, specify `ClusterAPI`.

    `status.authoritativeAPI`
    Specifies the value for the current authoritative API. This value indicates which API currently manages this resource. Do not change the value in this part of the specification.

    > [!IMPORTANT]
    > Do not change other values when you update the value of the `spec.authoritativeAPI` field. Because other controllers might process updates to other values before the synchronization controller processes the `spec.authoritativeAPI` field update, changing other values can cause unexpected behavior.
    >
    > For more information, see "Unexpected behavior when changing resource configurations".

</div>

<div>

<div class="title">

Verification

</div>

- Check the status of the conversion by running the following command:

  ``` terminal
  $ oc -n openshift-machine-api get <resource_kind>/<resource_name> -o json | jq .status.authoritativeAPI
  ```

  where:

  `<resource_kind>`
  Specifies a compute machine with `machine.machine.openshift.io` or compute machine set with `machineset.machine.openshift.io`.

  `<resource_name>`
  Specifies the name of the Machine API resource that you want to migrate to a Cluster API resource.

  - While the conversion progresses, this command returns a value of `Migrating`. If this value persists for a long time, check the logs for the `cluster-capi-operator` deployment in the `openshift-cluster-api` namespace for more information and to identify potential issues.

  - When the conversion is complete, this command returns a value of `ClusterAPI`.

- [Unexpected behavior when changing resource configurations](cluster-api-troubleshooting.md#ts-capi-migrate-unexpected-behavior_cluster-api-troubleshooting)

</div>

## Deploying Cluster API compute machines by using a Machine API compute machine set

You can configure a Machine API compute machine set to deploy Cluster API compute machines. With this process, you can test the Cluster API compute machine creation workflow without creating and scaling a Cluster API compute machine set.

A Machine API compute machine set with this configuration creates nonauthoritative Machine API compute machines that use the Cluster API as authoritative. The two-way synchronization controller then creates corresponding authoritative Cluster API machines that provision on the underlying infrastructure.

> [!IMPORTANT]
> Deploying Cluster API compute machines by using a Machine API compute machine set is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Prerequisites

</div>

- You have deployed an OpenShift Container Platform cluster on a supported infrastructure type.

- You have enabled the use of the Cluster API.

- You have enabled the `MachineAPIMigration` feature gate in the `TechPreviewNoUpgrade` feature set.

- You have access to the cluster using an account with `cluster-admin` permissions.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  List the Machine API compute machine sets in your cluster by running the following command:

    ``` terminal
    $ oc get machineset.machine.openshift.io -n openshift-machine-api
    ```

2.  Edit the resource specification by running the following command:

    ``` terminal
    $ oc edit machineset.machine.openshift.io <machine_set_name> \
      -n openshift-machine-api
    ```

    Replace `<machine_set_name>` with the name of the Machine API compute machine set that you want to configure to deploy Cluster API compute machines.

3.  In the resource specification, update the value of the `spec.template.spec.authoritativeAPI` field:

    ``` yaml
    apiVersion: machine.openshift.io/v1beta1
    kind: MachineSet
    metadata:
      [...]
      name: <machine_set_name>
      [...]
    spec:
      authoritativeAPI: MachineAPI
      [...]
      template:
        [...]
        spec:
          authoritativeAPI: ClusterAPI
    status:
      authoritativeAPI: MachineAPI
      [...]
    ```

    where:

    `spec.authoritativeAPI`
    Specifies the unconverted value for the Machine API compute machine set. Do not change the value in this part of the specification.

    `spec.template.spec.authoritativeAPI`
    Specifies the authoritative API for the machine set. To configure the compute machine set to deploy Cluster API compute machines, set this value to `ClusterAPI`.

    `status.authoritativeAPI`
    Specifies the current value for the Machine API compute machine set. Do not change the value in this part of the specification.

</div>

<div>

<div class="title">

Verification

</div>

1.  List the machines that are managed by the updated compute machine set by running the following command:

    ``` terminal
    $ oc get machines.machine.openshift.io \
      -n openshift-machine-api \
      -l machine.openshift.io/cluster-api-machineset=<machine_set_name>
    ```

2.  To verify that a machine created by the updated machine set has the correct configuration, examine the `status.authoritativeAPI` field in the CR for one of the new machines by running the following command:

    ``` terminal
    $ oc describe machines.machine.openshift.io <machine_name> \
      -n openshift-machine-api
    ```

    For a Cluster API compute machine, the value of the field is `ClusterAPI`.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Troubleshooting resource migration](cluster-api-troubleshooting.md#ts-capi-resource-migration_cluster-api-troubleshooting)

- [Migrating Cluster API resources to Machine API resources](cluster-api-disabling.md#capi-to-mapi-migration-overview_cluster-api-disabling)

</div>
