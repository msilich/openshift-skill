> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-con_requesting_persistent_storage_for_workspaces). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Persistent storage for workspaces

OpenShift Dev Spaces workspaces and workspace data are ephemeral and are lost when the workspace stops.

To preserve the workspace state in persistent storage while the workspace is stopped, request a Kubernetes PersistentVolume (PV). The PV is requested for the `Dev Workspace` containers in the OpenShift cluster of your organization’s OpenShift Dev Spaces instance.

You can request a PV by using the devfile or a Kubernetes PersistentVolumeClaim (PVC).

An example of a PV is the `/projects/` directory of a workspace, which is mounted by default for non-ephemeral workspaces.

Persistent Volumes come at a cost: attaching a persistent volume slows workspace startup. For more information about persistent storage on OpenShift, see Additional resources.

Warning

Starting another, concurrently running workspace with a `ReadWriteOnce` PV might fail.

**Related information**  

- [Red Hat OpenShift Documentation: Understanding persistent storage](https://docs.openshift.com/container-platform/4.22/storage/understanding-persistent-storage.html)
- [Kubernetes Documentation: Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
