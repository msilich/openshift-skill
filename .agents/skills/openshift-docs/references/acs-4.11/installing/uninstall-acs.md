<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Uninstalling Red Hat Advanced Cluster Security for Kubernetes involves deleting all resources that Red Hat Advanced Cluster Security for Kubernetes creates during installation.

<a id="uninstall-acs-overview_uninstall-acs"></a>

# Resources created during installation

When you install Red Hat Advanced Cluster Security for Kubernetes, it creates several resources across your cluster that you must remove during uninstallation.

Red Hat Advanced Cluster Security for Kubernetes creates the following resources:

- A namespace called `rhacs-operator` where you install the Operator, if you chose the Operator method of installation

- A namespace called `stackrox`, or another namespace where you created the Central and SecuredCluster custom resources

- `PodSecurityPolicy` and Kubernetes role-based access control (RBAC) objects for all components

- Additional labels on namespaces, for use in generated network policies

- An application custom resource definition (CRD), if it does not exist

Uninstalling Red Hat Advanced Cluster Security for Kubernetes involves deleting all of these items.

<a id="delete-acs-namespace_uninstall-acs"></a>

# Deleting the namespace

You can delete the namespace that Red Hat Advanced Cluster Security for Kubernetes creates by using the OpenShift Container Platform or Kubernetes command-line interface.

<div>

<div class="title">

Procedure

</div>

- Delete the `stackrox` namespace:

  - On OpenShift Container Platform:

    ``` terminal
    $ oc delete namespace stackrox
    ```

  - On Kubernetes:

    ``` terminal
    $ kubectl delete namespace stackrox
    ```

    > [!NOTE]
    > If you installed RHACS in a different namespace, use the name of that namespace in the `delete` command.

</div>

<a id="delete-acs-global-resources_uninstall-acs"></a>

# Deleting global resources

You can delete the global resources that Red Hat Advanced Cluster Security for Kubernetes (RHACS) creates by using the OpenShift Container Platform or Kubernetes command-line interface (CLI).

<div>

<div class="title">

Procedure

</div>

- To delete the global resources by using the OpenShift Container Platform CLI, perform the following steps:

  1.  Retrieve all the StackRox-related cluster roles, cluster role bindings, roles, role bindings, and PSPs, and then delete them by running the following command:

      ``` terminal
      $ oc get clusterrole,clusterrolebinding,role,rolebinding,psp -o name | grep stackrox | xargs oc delete --wait
      ```

      > [!NOTE]
      > You might receive the `error: the server doesn’t have a resource type "psp"` error message in RHACS 4.4 and later versions because the pod security policies (PSPs) are deprecated. Kubernetes removed the PSPs in version 1.25, except for clusters with older Kubernetes versions.

  2.  Delete the custom security context constraints (SCCs) labeled with `app.kubernetes.io/name=stackrox` by running the following command:

      ``` terminal
      $ oc delete scc -l "app.kubernetes.io/name=stackrox"
      ```

      > [!NOTE]
      > You might receive the `No resources found` error message in RHACS 4.4 and later versions because the custom SCCs with this label are no longer used in these versions.

  3.  Delete the `ValidatingWebhookConfiguration` object named `stackrox` by running the following command:

      ``` terminal
      $ oc delete ValidatingWebhookConfiguration stackrox
      ```

- To delete the global resources by using the Kubernetes CLI, perform the following steps:

  1.  Retrieve all the StackRox-related cluster roles, cluster role bindings, roles, role bindings, and PSPs, and then delete them by running the following command:

      ``` terminal
      $ kubectl get clusterrole,clusterrolebinding,role,rolebinding,psp -o name | grep stackrox | xargs kubectl delete --wait
      ```

      > [!NOTE]
      > You might receive the `error: the server doesn’t have a resource type "psp"` error message in RHACS 4.4 and later versions because the pod security policies (PSPs) are deprecated. Kubernetes removed the PSPs in version 1.25, except for clusters with older Kubernetes versions.

  2.  Delete the `ValidatingWebhookConfiguration` object named `stackrox` by running the following command:

      ``` terminal
      $ kubectl delete ValidatingWebhookConfiguration stackrox
      ```

</div>

<a id="delete-acs-label-annotation_uninstall-acs"></a>

# Deleting labels and annotations

You can delete the labels and annotations that Red Hat Advanced Cluster Security for Kubernetes creates, by using the OpenShift Container Platform or Kubernetes command-line interface.

<div>

<div class="title">

Procedure

</div>

- Delete labels and annotations:

  - On OpenShift Container Platform:

    ``` terminal
    $ for namespace in $(oc get ns | tail -n +2 | awk '{print $1}'); do     oc label namespace $namespace namespace.metadata.stackrox.io/id-;     oc label namespace $namespace namespace.metadata.stackrox.io/name-;     oc annotate namespace $namespace modified-by.stackrox.io/namespace-label-patcher-;   done
    ```

  - On Kubernetes:

    ``` terminal
    $ for namespace in $(kubectl get ns | tail -n +2 | awk '{print $1}'); do     kubectl label namespace $namespace namespace.metadata.stackrox.io/id-;     kubectl label namespace $namespace namespace.metadata.stackrox.io/name-;     kubectl annotate namespace $namespace modified-by.stackrox.io/namespace-label-patcher-;   done
    ```

</div>
