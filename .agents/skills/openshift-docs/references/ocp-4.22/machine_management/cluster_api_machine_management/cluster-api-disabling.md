<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To stop using the Cluster API to automate the management of infrastructure resources on your OpenShift Container Platform cluster, convert any Cluster API resources on your cluster to equivalent Machine API resources.

> [!IMPORTANT]
> Managing machines with the Cluster API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

# Cluster API resources migration to Machine API resources

On clusters that support migrating between the Cluster API and Machine API resources, the two-way synchronization controller supports converting a Cluster API resource to a Machine API resource.

> [!NOTE]
> The two-way synchronization controller only operates on clusters with the `MachineAPIMigration` feature gate in the `TechPreviewNoUpgrade` feature set enabled.

You can migrate resources that you originally migrated from the Machine API to the Cluster API, or resources that you created as Cluster API resources initially. Migrating an original Machine API resource to a Cluster API resource and then migrating it back provides an opportunity to verify that the migration process works as expected.

> [!NOTE]
> You can only migrate some resources on supported infrastructure types.

| Infrastructure | Compute machine | Compute machine set | Machine health check | Control plane machine set | Cluster autoscaler |
|----|----|----|----|----|----|
| AWS | Technology Preview | Technology Preview | Not Available | Not Available | Not Available |
| All other infrastructure types | Not Available | Not Available | Not Available | Not Available | Not Available |

Supported resource conversions

## Migrating a Cluster API resource to use the Machine API

You can migrate individual Cluster API objects to equivalent Machine API objects.

> [!IMPORTANT]
> Migrating a Cluster API resource to use the Machine API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Prerequisites

</div>

- You have deployed an OpenShift Container Platform cluster on a supported infrastructure type.

- You have enabled the `MachineAPIMigration` feature gate in the `TechPreviewNoUpgrade` feature set.

- You have access to the cluster using an account with `cluster-admin` permissions.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Identify the Cluster API resource that you want to migrate to a Machine API resource by running the following command:

    ``` terminal
    $ oc get <resource_kind> -n openshift-cluster-api
    ```

    where `<resource_kind>` is one of the following values:

    `machine.cluster.x-k8s.io`
    The fully qualified name of the resource kind for a compute or control plane machine.

    `machineset.cluster.x-k8s.io`
    The fully qualified name of the resource kind for a compute machine set.

2.  Edit the resource specification by running the following command:

    ``` terminal
    $ oc edit <resource_kind>/<resource_name> -n openshift-machine-api
    ```

    where:

    `<resource_kind>`
    Specifies a compute machine with `machine.machine.openshift.io` or compute machine set with `machineset.machine.openshift.io`.

    `<resource_name>`
    Specifies the name of the Machine API resource that corresponds to the Cluster API resource that you want to migrate to the Machine API.

3.  In the resource specification, update the value of the `spec.authoritativeAPI` field:

    ``` yaml
    apiVersion: machine.openshift.io/v1beta1
    kind: <resource_kind>
    metadata:
      name: <resource_name>
      [...]
    spec:
      authoritativeAPI: MachineAPI
      [...]
    status:
      authoritativeAPI: ClusterAPI
      [...]
    ```

    where:

    `kind`
    Specifies the resource kind of the resource that you want to migrate. For example, the resource kind for a compute machine set is `MachineSet` and the resource kind for a compute machine is `Machine`.

    `metadata.name`
    Specifies the name of the resource that you want to migrate.

    `spec.authoritativeAPI`
    Specifies the authoritative API that you want this resource to use. For example, to start migrating a Cluster API resource to the Machine API, specify `MachineAPI`.

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
  Specifies the name of the Machine API resource that corresponds to the Cluster API resource that you want to migrate to the Machine API.

  - While the conversion progresses, this command returns a value of `Migrating`. If this value persists for a long time, check the logs for the `cluster-capi-operator` deployment in the `openshift-cluster-api` namespace for more information and to identify potential issues.

  - When the conversion is complete, this command returns a value of `MachineAPI`.

  > [!IMPORTANT]
  > Do not delete any nonauthoritative resource that does not use the current authoritative API unless you want to delete the corresponding resource that does use the current authoritative API.
  >
  > When you delete a nonauthoritative resource that does not use the current authoritative API, the synchronization controller deletes the corresponding resource that does use the current authoritative API. For more information, see "Unexpected resource deletion behavior" in the *Troubleshooting resource migration* content.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Unexpected behavior when changing resource configurations](cluster-api-troubleshooting.md#ts-capi-migrate-unexpected-behavior_cluster-api-troubleshooting)

</div>

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

<div>

<div class="title">

Additional resources

</div>

- [Troubleshooting resource migration](cluster-api-troubleshooting.md#ts-capi-resource-migration_cluster-api-troubleshooting)

- [Machine API to Cluster API resource migration](cluster-api-getting-started.md#mapi-to-capi-migration-overview_cluster-api-getting-started)

</div>
