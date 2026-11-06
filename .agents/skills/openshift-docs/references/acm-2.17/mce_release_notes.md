> Source: [Red Hat Advanced Cluster Management for Kubernetes 2.17](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/mce_release_notes/index). Copyright Red Hat.
> Adapted from AsciiDoc to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md), [CC BY-SA 3.0](LICENSE.md) and SOURCE.json for source revisions and gaps.

<a id="mce-release-notes-intro"></a>

# Release notes for the multicluster engine operator

Learn about new features and enhancements, support, deprecations, removals, and fixed issues for Cluster lifecycle with multicluster engine operator version 2.11.

- [New features and enhancements for the multicluster engine operator](mce_release_notes.md#new-features-mce)

- [Fixed issues for Cluster lifecycle with multicluster engine operator](mce_release_notes.md#errata-updates-mce)

- [Known issues for Cluster lifecycle with multicluster engine operator](mce_release_notes.md#known-issues-mce)

- [Deprecations and removals for Cluster lifecycle with multicluster engine operator](mce_release_notes.md#deprecations-removals-cluster-mce)

**Important:**

- OpenShift Container Platform release notes are *not* documented in this product documentation. For your OpenShift Container Platform cluster, see [OpenShift Container Platform release notes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20).

- **Deprecated:** multicluster engine operator 2.4 and earlier versions are no longer supported. The documentation might remain available, but without any errata releases for fixed issues or other updates. **Best practice:** Upgrade to the most recent version.

- The documentation references the earliest supported OpenShift Container Platform version, unless a specific component or function is introduced and tested only on a more recent version of OpenShift Container Platform.

- For full support information, see the [multicluster engine operator Support Matrix](https://access.redhat.com/articles/7142379). For lifecycle information, see [Red Hat OpenShift Container Platform Life Cycle policy](https://access.redhat.com/support/policy/updates/openshift).

- If you experience issues with one of the currently supported releases, or the product documentation, go to [Red Hat Support](https://www.redhat.com/en/services/support) where you can troubleshoot, view *Knowledgebase* articles, connect with the Support Team, or open a case. You must log in with your credentials.

- You can also learn more about the Customer Portal documentation at [Red Hat Customer Portal FAQ](https://access.redhat.com/articles/33844).

<a id="new-features-mce"></a>

## New features and enhancements for the multicluster engine operator

Learn about multicluster engine for Kubernetes operator 2.11 new features and enhancements, support, deprecations, removals, and fixed issues for errata releases.

multicluster engine operator version 2.11 is released with Red Hat Advanced Cluster Management version 2.16 for Cluster lifecycle management, but you can use stand-alone multicluster engine operator with your OpenShift Container Platform hub cluster, as well.

For full support information, including supported OpenShift Container Platform versions, see the [multicluster engine operator Support Matrix](https://access.redhat.com/articles/7142379). For lifecycle information, see [Red Hat OpenShift Container Platform Life Cycle policy](https://access.redhat.com/support/policy/updates/openshift).

Use multicluster engine operator features for creating, importing, managing, and destroying Kubernetes clusters across various infrastructure cloud providers, private clouds, and on-premises data centers.

If you are using multicluster engine operator with Red Hat Advanced Cluster Management installed afterwards, see the [New features and enhancements for Red Hat Advanced Cluster Management](release_notes.md#new-features-acm) this release.

**Important:**

- Cluster management supports all providers that are certified through the Cloud Native Computing Foundation (CNCF) Kubernetes Conformance Program. Choose a vendor that is recognized by CNCF for your hybrid cloud multicluster management. See the following information about using CNCF providers:

- Learn how CNCF providers are certified at [Certified Kubernetes Conformance](https://www.cncf.io/training/certification/software-conformance/).

- For Red Hat support information about CNCF third-party providers, see [Red Hat support with third party components](https://access.redhat.com/articles/third-party-software-support), or [Contact Red Hat support](https://access.redhat.com/support/contact/).

- If you bring your own CNCF conformance certified cluster, you need to change the OpenShift Container Platform CLI `oc` command to the Kubernetes CLI command, `kubectl`.

- Some features and components are identified and released as [Technology Preview](https://access.redhat.com/support/offerings/techpreview).

- New features and enhancements for multicluster engine operator 2.11 include the following changes:

  - **Technology Preview:** You can now install on-premises OpenShift Container Platform clusters with third-party Container Network Interface (CNI) plugins to maintain operational consistency or use special network functions. See [Configuring third-party CNI plugins for on-premises cluster installation (Technology Preview)](clusters.md#config-third-party-cni-on-prem) to learn more.

<a id="errata-updates-mce"></a>

## Fixed issues for Cluster lifecycle with multicluster engine operator

By default, fixed issues for *errata* releases are automatically applied when released. The details are published here when the release is available. If no release notes are listed, the product does not have an errata release at this time.

**Important:** For reference, Jira links and Jira numbers might be added to the content and used internally. Links that require access might not be available for the user. Learn about the types of [errata releases](https://access.redhat.com/security/updates/advisory) from Red Hat.

- Errata 2.17.1

  - Delivers updates to one or more product container images.

<a id="known-issues-mce"></a>

## Known issues for Cluster lifecycle with multicluster engine operator

Review the Known issues for *Cluster lifecycle with multicluster engine operator* for this release, or known issues that continued from the previous release.

Cluster management known issues and limitations are part of the *Cluster lifecycle with multicluster engine operator* documentation. Known issues for multicluster engine operator integrated *with* Red Hat Advanced Cluster Management are documented in the [Release notes for Red Hat Advanced Cluster Management](release_notes.md#acm-release-notes).

**Important:** OpenShift Container Platform release notes are not documented in this product documentation. For your OpenShift Container Platform cluster, see [OpenShift Container Platform release notes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.17).

- [HyperShift not supported on Red Hat Enterprise Linux 10 with certain feature gates](mce_release_notes.md#hypershift-rhel10-feature-gates)

- [Unclaimed Hive clusters recreated during ClusterPool custom resource definition changes](mce_release_notes.md#recreated-hive-clusters)

- [*installNamespace* field can only have one value](mce_release_notes.md#installnamespace-one-value)

- [Cluster API Provider Metal3 certificate generation fails after upgrade](mce_release_notes.md#capm3-cert-generation-fails)

- [Cluster API and Cluster API Provider for Azure deployments not creating pods](mce_release_notes.md#capi-azure-pods-not-created)

- [HyperShift conflict when creating Azure Red Hat OpenShift hosted control plane clusters with Cluster API Provider for Azure](mce_release_notes.md#hypershift-aro-hcp-conflict)

- [Microsoft Azure authentication fails when creating Azure Red Hat OpenShift hosted control plane clusters with Cluster API Provider for Azure](mce_release_notes.md#azure-auth-aro-hcp)

- [Resource deletion during cluster distribution updates](mce_release_notes.md#resource-deletion-cluster-distribution)

- [HyperShift operator and Cluster API components conflict](mce_release_notes.md#hypershift-capi-conflict)

- [HyperShift operator does not receive infrastructure node configuration](mce_release_notes.md#hypershift-infra-node-config)

- [HyperShift installation fails on Red Hat OpenShift Service on AWS (classic) due to admission webhook error](mce_release_notes.md#hypershift-rosa-webhook)

- [*ClusterCurator* status stuck when updating the hub cluster](mce_release_notes.md#clustercurator-stuck-hub-update)

- [Klusterlet add-on does not tolerate `node-role.kubernetes.io/infra` taint with `NoExecute` effect](mce_release_notes.md#klusterlet-noexecute-taint)

- [Limitation with *nmstate*](mce_release_notes.md#limitation-with-nmstate)

- [Deleting a managed cluster set does not automatically remove its label](mce_release_notes.md#clusterset-label-not-removed)

- [ClusterClaim error](mce_release_notes.md#hive-cluster-claim)

- [Product channel out of sync with provisioned cluster](mce_release_notes.md#channel-out-of-sync)

- [Cluster provision with Ansible automation fails in proxy environment](mce_release_notes.md#cluster-provision-fails-ansible-proxy)

- [Cannot delete managed cluster namespace manually](mce_release_notes.md#cannot-delete-managed-cluster-namespace)

- [Automatic secret updates for provisioned clusters not supported](mce_release_notes.md#automatic-secret-updates-unsupported)

- [Process to destroy a cluster does not complete](mce_release_notes.md#destroy-cluster-incomplete)

- [Cannot update OpenShift Container Platform Dedicated managed clusters with the console](mce_release_notes.md#cannot-update-osd-console)

- [Non-OpenShift Container Platform managed clusters require *ManagedServiceAccount* or *LoadBalancer* for pod logs](mce_release_notes.md#non-ocp-pod-logs)

- [Client cannot reach iPXE script](mce_release_notes.md#cannot-reach-ipxe-script)

- [ManagedClusterSet API specification limitation](mce_release_notes.md#managedclusterset-api-limitation)

- [Cluster curator does not support OpenShift Container Platform Dedicated clusters](mce_release_notes.md#clustercurator-osd-unsupported)

- [Custom ingress domain not applied correctly](mce_release_notes.md#custom-ingress-domain)

- [*tolerations* and *nodeSelector* settings do not affect the *managed-serviceaccount* agent](mce_release_notes.md#settings-limit-msa-agent)

- [Assisted Installer pulls incorrect cached image in disconnected environments](mce_release_notes.md#assisted-incorrect-cached-image)

- [single-node OpenShift cluster installation requires matching OpenShift Container Platform with infrastructure operator for Red Hat OpenShift](mce_release_notes.md#install-sno-ocp-infra)

- [Cannot use host inventory to boot with the discovery image and add hosts automatically](mce_release_notes.md#boot-discovery-auto-add-host)

- [Nodes shut down after removing `BareMetalHost` resource](mce_release_notes.md#nodes-shut-down-bmh)

- [Managed cluster fails to rejoin hub cluster after Image-Based Break/Fix server replacement](mce_release_notes.md#stale-neighbor-cache-rejoin)

<a id="hypershift-rhel10-feature-gates"></a>

### HyperShift not supported on Red Hat Enterprise Linux 10 with certain feature gates

You cannot use enable the hosted control plane feature on OpenShift Container Platform version 4.22 clusters that run on Red Hat Enterprise Linux 10 if the `TechPreviewNoUpgrade` feature gate is enabled. If you attempt to enable hosted control plane on these clusters, the clusters become unstable.

<div>

<div class="title">

Additional resources

</div>

- [ACM-34084](https://issues.redhat.com/browse/ACM-34084)

</div>

<a id="recreated-hive-clusters"></a>

### Unclaimed Hive clusters recreated during ClusterPool custom resource definition changes

During a multicluster engine operator upgrade or modification to the `ClusterPool` custom resource definition, Hive might delete and re-create all unclaimed clusters. This is expected behavior and ensures that unclaimed clusters reflect the latest configuration defined in the updated `ClusterPool` resource specification.

<div>

<div class="title">

Additional resources

</div>

- [ACM-21686](https://issues.redhat.com/browse/ACM-21686)

</div>

<a id="installnamespace-one-value"></a>

### *installNamespace* field can only have one value

**Note:** The `spec.installNamespace` field is deprecated. See [Product deprecations and removals](mce_release_notes.md#deprecations-removals-cluster-mce) to learn more.

When enabling the `managed-serviceaccount` add-on, the `installNamespace` field in the `ManagedClusterAddOn` resource must have `open-cluster-management-agent-addon` as the value. Other values are ignored. The `managed-serviceaccount` add-on agent is always deployed in the `open-cluster-management-agent-addon` namespace on the managed cluster.

<div>

<div class="title">

Additional resources

</div>

- [ACM-7523](https://issues.redhat.com/browse/ACM-7523)

</div>

<a id="capm3-cert-generation-fails"></a>

### Cluster API Provider Metal3 certificate generation fails after upgrade

After you upgrade from multicluster engine for Kubernetes operator version 2.10 or 2.10.1 to version 2.11, the automatic generation of certificates for the Cluster API Provider Metal3 webhooks fail due to a naming conflict in the target resources. As a result, webhooks do not validate.

To resolve the issue, manually delete the existing secret and the renamed service. The operator then regenerates the correct secret. Complete the following steps on your managed cluster:

<div>

<div class="title">

Procedure

</div>

1.  Delete the webhook service. Run the following command:

    ``` bash
    oc delete service capm3-webhook-service -n multicluster-engine
    ```

2.  Delete the Transport Layer Security (TLS) secret. Run the following command:

    ``` bash
    oc delete secret capm3-webhook-service-cert -n multicluster-engine
    ```

3.  Clear the error annotations. Run the following command:

    ``` bash
    oc annotate service mce-capm3-webhook-service -n multicluster-engine \
    service.alpha.openshift.io/serving-cert-generation-error- \
    service.alpha.openshift.io/serving-cert-generation-error-num- \
    service.beta.openshift.io/serving-cert-generation-error- \
    service.beta.openshift.io/serving-cert-generation-error-num-
    ```

4.  Delete the stale webhook configurations. Run the following commands:

    ``` bash
    oc delete mutatingwebhookconfiguration capm3-mutating-webhook-configuration
    ```

    <!-- Separate adjacent source examples. -->

    ``` bash
    oc delete validatingwebhookconfiguration capm3-validating-webhook-configuration
    ```

5.  Delete the new TLS secret. Run the following command:

    ``` bash
    oc delete secret mce-capm3-webhook-service-cert -n multicluster-engine
    ```

6.  Restart the pod to regenerate the certificate. Run the following command:

    ``` bash
    oc delete pod mce-capm3-controller-manager-<hash> -n multicluster-engine
    ```

7.  Delete the old `controller-manager` deployment. Run the following command:

    ``` bash
    oc delete deployment capm3-controller-manager -n multicluster-engine
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [MGMT-23257](https://redhat.atlassian.net/browse/MGMT-23257)

</div>

<a id="capi-azure-pods-not-created"></a>

### Cluster API and Cluster API Provider for Azure deployments not creating pods

When you deploy `cluster-api` and `cluster-api-provider-azure` components, the Cluster API controllers might not create pods. To work around the issue, complete the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Verify that the `cluster-api` component is enabled. Run the following command:

    ``` bash
    oc get mce multiclusterengine -o json | \
      jq -r '.spec.overrides.components[] | select(.name | contains("cluster-api"))'
    ```

2.  Check if the `hypershift` component is causing a conflict. Run the following command to check if the `READY` status is `0/1`:

    ``` bash
    oc get deployment -n hypershift
    ```

3.  If the status is `0/1`, force multicluster engine operator reconciliation. Run the following command:

    ``` bash
    oc annotate mce multiclusterengine force-reconcile=$(date +%s) --overwrite
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-30244](https://issues.redhat.com/browse/ACM-30244)

</div>

<a id="hypershift-aro-hcp-conflict"></a>

### HyperShift conflict when creating Azure Red Hat OpenShift hosted control plane clusters with Cluster API Provider for Azure

You might not be able to create Azure Red Hat OpenShift hosted control plane clusters by using Cluster API Provider for Azure if the `hypershift` and `cluster-api` controllers are running at the same time. To resolve the issue, complete the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Disable the `hypershift` component. Run the following command:

    ``` bash
    oc patch mce multiclusterengine --type=merge -p "{\"spec\":{\"overrides\":{\"components\":$(oc get mce multiclusterengine -o json | jq -c '.spec.overrides.components | map(if .name == "hypershift" then .enabled = false else . end)')}}}"
    ```

2.  Disable the `hypershift-local-hosting` component. Run the following command:

    ``` bash
    oc patch mce multiclusterengine --type=merge -p "{\"spec\":{\"overrides\":{\"components\":$(oc get mce multiclusterengine -o json | jq -c '.spec.overrides.components | map(if .name == "hypershift-local-hosting" then .enabled = false else . end)')}}}"
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-30244](https://issues.redhat.com/browse/ACM-30244)

</div>

<a id="azure-auth-aro-hcp"></a>

### Microsoft Azure authentication fails when creating Azure Red Hat OpenShift hosted control plane clusters with Cluster API Provider for Azure

When you create Azure Red Hat OpenShift hosted control plane clusters by using Cluster API Provider for Azure, the cluster creation might fail because of Microsoft Azure authentication errors. To work around the issue, ensure you are connected to Microsoft Azure with your credentials. Complete the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Verify your Microsoft Azure credentials secret. Run the following command. Replace `<cluster-namespace>` with the namespace of your cluster:

    ``` bash
    oc get secret aso-credential -n <cluster-namespace> -o yaml
    ```

2.  Test the Microsoft Azure connection. Run the following command:

    ``` bash
    oc run azure-cli --rm -it --image=mcr.microsoft.com/azure-cli -- bash
    ```

3.  Log in to Microsoft Azure inside the pod. Run the following command. Replace `<client_id>`, `<client_secret>`, and `<tenant_id>` with your Microsoft Azure credentials:

    ``` bash
    az login --service-principal --username <client_id> --password <client_secret> --tenant <tenant_id>
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-30244](https://issues.redhat.com/browse/ACM-30244)

</div>

<a id="resource-deletion-cluster-distribution"></a>

### Resource deletion during cluster distribution updates

When a change occurs in the cluster because of the `Placement` resource, cluster redistribution occurs across multiple `PlacementDecisions` resources. During the sequential update, a cluster is temporarily missing from all `PlacementDecisions` resources. Controllers that monitor `PlacementDecisions` resources identify this temporary deletion as cluster removal. This sequence leads to unnecessary resource deletion and recreation. For example, the `addon-management-controller` deletes and re-creates `ManagedClusterAddOns`, which cause workload disruption.

<div>

<div class="title">

Additional resources

</div>

- [ACM-27799](https://issues.redhat.com/browse/ACM-27799)

</div>

<a id="hypershift-capi-conflict"></a>

### HyperShift operator and Cluster API components conflict

Red Hat Advanced Cluster Management and multicluster engine operator enable the `hypershift` and `hypershift-local-hosting` components by default, which can conflict with the `cluster-api` and `cluster-api-provider-aws` components. When you enable and then disable the `cluster-api` and `cluster-api-provider-aws` components, custom resource definitions of a higher version might remain in the cluster. Manually remove the custom resource definitions before you re-enable the `hypershift-local-hosting` component. To manage Red Hat OpenShift Service on AWS (classic) clusters by using the `cluster-api` and `cluster-api-provider-aws` components, you must disable the `hypershift` and `hypershift-local-hosting` components to prevent API conflicts.

<div>

<div class="title">

Procedure

</div>

1.  Run the following command to remove the custom resource definitions:

    ``` bash
    oc delete crd <crd-name>
    ```

2.  Remove the following custom resource definitions:

    - `clusterresourcesetbindings.addons.cluster.x-k8s.io`

    - `clusterresourcesets.addons.cluster.x-k8s.io`

    - `clusters.cluster.x-k8s.io`

    - `clusterclasses.cluster.x-k8s.io`

    - `machines.cluster.x-k8s.io`

    - `machinesets.cluster.x-k8s.io`

    - `machinedeployments.cluster.x-k8s.io`

    - `machinepools.cluster.x-k8s.io`

    - `machinehealthchecks.cluster.x-k8s.io`

    - `machinedrainrules.cluster.x-k8s.io`

</div>

<a id="hypershift-infra-node-config"></a>

### HyperShift operator does not receive infrastructure node configuration

When Red Hat Advanced Cluster Management or multicluster engine operator is installed with infrastructure node selection configured, by using `nodeSelector` and `tolerations` for infrastructure node, the HyperShift operator deployment does not receive the settings.

Even if the `multicluster engine` subscription is configured to place pods on infrastructure nodes by using `nodeSelector` and `tolerations`, the HyperShift operator pods are scheduled on regular worker nodes instead of the designated infrastructure nodes.

The HyperShift operator deployment does not automatically propagate the infrastructure node placement configuration from the subscription.

<div>

<div class="title">

Procedure

</div>

1.  After you install the HyperShift add-on, manually patch the HyperShift operator deployment to add the infrastructure node selector and tolerations.

2.  Apply a patch to the operator deployment in the `hypershift` namespace by running the following command with the specifications for your infrastructure nodes. The manual patch ensures that the operator pods are placed on the correct nodes to comply with your infrastructure requirements.

    ``` bash
    oc patch deployment operator -n hypershift --type=merge -p '{"spec":{"template":{"spec":{"nodeSelector":{"node-role.kubernetes.io/infra":""},"tolerations":[{"key":"node-role.kubernetes.io/infra","operator":"Exists","effect":"NoSchedule"}]}}}}'
    ```

    See the following example of a patch that adds the infrastructure node selector and tolerations to the HyperShift operator deployment:

    ``` yaml
          nodeSelector:
            node-role.kubernetes.io/infra: ""
          tolerations:
          - key: node-role.kubernetes.io/infra
            operator: Exists
            effect: NoSchedule
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-24191](https://issues.redhat.com/browse/ACM-24191)

</div>

<a id="hypershift-rosa-webhook"></a>

### HyperShift installation fails on Red Hat OpenShift Service on AWS (classic) due to admission webhook error

When you install multicluster engine for Kubernetes operator 2.10 on Red Hat OpenShift Service on AWS (classic), the HyperShift installation job might fail repeatedly with an admission webhook error similar to the following message: `namespace-validation.managed.openshift.io denied the request`. See the following explanations for the error. To resolve this issue, create a `ConfigMap` in the `local-cluster` namespace to disable platform monitoring.

- The installation process attempts to create a `hypershift` namespace that includes the `openshift.io/cluster-monitoring: "true"` label.

- The Red Hat OpenShift Service on AWS (classic) managed admission webhooks prevent users from modifying protected labels on namespaces, including the `cluster-monitoring` label.

- The platform monitoring flag defaults to monitoring the operator, which adds the `cluster-monitoring` label to the `hypershift` namespace.

- In managed environments, such as Red Hat OpenShift Service on AWS (classic), the service provider typically handles platform-level monitoring. Therefore, this monitoring is not required and conflicts with namespace protection policies.

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file for the `ConfigMap` with the following content:

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: hypershift-operator-install-flags
      namespace: local-cluster
    data:
      installFlagsToAdd: "--platform-monitoring=None"
      installFlagsToRemove: ""
    ```

2.  Apply the `ConfigMap` to your cluster to instruct the HyperShift installer to skip the `cluster-monitoring` label, which avoids the admission webhook conflict. Run the following command. Replace `<filename>` with the name of your YAML file:

    ``` bash
    oc apply -f <filename>.yaml
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-26040](https://issues.redhat.com/browse/ACM-26040)

</div>

<a id="clustercurator-stuck-hub-update"></a>

### *ClusterCurator* status stuck when updating the hub cluster

When you use the `ClusterCurator` resource to upgrade the hub cluster, the `ClusterCurator` status becomes stuck, even if the upgrade is successful. During upgrade, the hub cluster reboots, which stops the `Job` resource pod monitoring. To work around the issue, manually upgrade the hub cluster.

<div>

<div class="title">

Procedure

</div>

- If you already used the cluster curator to upgrade the hub cluster, you must delete the `ClusterCurator` resource hub cluster namespace so that future upgrades appear in the console.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-26863](https://issues.redhat.com/browse/ACM-26863)

</div>

<a id="klusterlet-noexecute-taint"></a>

### Klusterlet add-on does not tolerate `node-role.kubernetes.io/infra` taint with `NoExecute` effect

If you use the `node-role.kubernetes.io/infra` taint with the `NoExecute` effect on your infrastructure nodes, your add-on pods might become stuck.

<div>

<div class="title">

Procedure

</div>

- To work around the issue, either use the `NoSchedule` effect instead of `NoExecute` for the `node-role.kubernetes.io/infra` taint, or remove the `node-role.kubernetes.io/infra` taint from your infrastructure nodes.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-15906](https://issues.redhat.com/browse/ACM-15906)

</div>

<a id="limitation-with-nmstate"></a>

### Limitation with *nmstate*

Develop quicker by configuring copy and paste features. To configure the `copy-from-mac` feature in the `assisted-installer`, you must add the `mac-address` to the `nmstate` definition interface and the `mac-mapping` interface. The `mac-mapping` interface is provided outside the `nmstate` definition interface. As a result, you must provide the same `mac-address` twice.

<div>

<div class="title">

Additional resources

</div>

- [ACM-9128](https://issues.redhat.com/browse/ACM-9128)

</div>

<a id="clusterset-label-not-removed"></a>

### Deleting a managed cluster set does not automatically remove its label

After you delete a `ManagedClusterSet`, the label that is added to each managed cluster that associates the cluster to the cluster set is not automatically removed.

<div>

<div class="title">

Procedure

</div>

- Manually remove the label from each of the managed clusters that were included in the deleted managed cluster set. The label resembles the following example: `cluster.open-cluster-management.io/clusterset:<ManagedClusterSet Name>`.

</div>

<div>

<div class="title">

Additional resources

</div>

- [GH-20727](https://github.com/stolostron/backlog/issues/20727)

</div>

<a id="hive-cluster-claim"></a>

### ClusterClaim error

If you create a Hive `ClusterClaim` against a `ClusterPool` and manually set the `ClusterClaimspec` lifetime field to an invalid golang time value, the product stops fulfilling and reconciling all `ClusterClaims`, not just the malformed claim.

You see the following error in the `clusterclaim-controller` pod logs, which is a specific example with the `PoolName` and invalid `lifetime` included:

\+

``` bash
E0203 07:10:38.266841       1 reflector.go:138] sigs.k8s.io/controller-runtime/pkg/cache/internal/informers_map.go:224: Failed to watch *v1.ClusterClaim: failed to list *v1.ClusterClaim: v1.ClusterClaimList.Items: []v1.ClusterClaim: v1.ClusterClaim.v1.ClusterClaim.Spec: v1.ClusterClaimSpec.Lifetime: unmarshalerDecoder: time: unknown unit "w" in duration "1w", error found in #10 byte of ...|time":"1w"}},{"apiVe|..., bigger context ...|clusterPoolName":"policy-aas-hubs","lifetime":"1w"}},{"apiVersion":"hive.openshift.io/v1","kind":"Cl|...
```

<div>

<div class="title">

Procedure

</div>

- Delete the invalid claim. If the malformed claim is deleted, claims begin successfully reconciling again without any further interaction.

</div>

<div>

<div class="title">

Additional resources

</div>

- [GH-19968](https://github.com/stolostron/backlog/issues/19968)

</div>

<a id="channel-out-of-sync"></a>

### Product channel out of sync with provisioned cluster

The `clusterimageset` is in `fast` channel, but the provisioned cluster is in `stable` channel. Currently the product does not sync the `channel` to the provisioned OpenShift Container Platform cluster. Change to the right channel in the OpenShift Container Platform console. Click **Administration** \> **Cluster Settings** \> **Details Channel**.

<div>

<div class="title">

Additional resources

</div>

- [GH-18380](https://github.com/stolostron/backlog/issues/18380)

</div>

<a id="cluster-provision-fails-ansible-proxy"></a>

### Cluster provision with Ansible automation fails in proxy environment

An Automation template that is configured to automatically provision a managed cluster might fail when both of the following conditions are met:

- The hub cluster has cluster-wide proxy enabled.

- The Ansible Automation Platform can only be reached through the proxy.

<div>

<div class="title">

Additional resources

</div>

- [GH-17659](https://github.com/stolostron/backlog/issues/17659)

</div>

<a id="cannot-delete-managed-cluster-namespace"></a>

### Cannot delete managed cluster namespace manually

You cannot delete the namespace of a managed cluster manually. The managed cluster namespace is automatically deleted after the managed cluster is detached. If you delete the managed cluster namespace manually before the managed cluster is detached, the managed cluster shows a continuous terminating status after you delete the managed cluster. To delete this terminating managed cluster, manually remove the finalizers from the managed cluster that you detached.

<div>

<div class="title">

Additional resources

</div>

- [GH-13474](https://github.com/stolostron/backlog/issues/13474)

</div>

<a id="automatic-secret-updates-unsupported"></a>

### Automatic secret updates for provisioned clusters not supported

When you change your cloud provider access key on the cloud provider side, you also need to update the corresponding credential for this cloud provider on the console of multicluster engine operator. This is required when your credentials expire on the cloud provider where the managed cluster is hosted and you try to delete the managed cluster.

<div>

<div class="title">

Additional resources

</div>

- [GH-3706](https://github.com/stolostron/backlog/issues/3706)

</div>

<a id="destroy-cluster-incomplete"></a>

### Process to destroy a cluster does not complete

When you destroy a managed cluster, the status continues to display `Destroying` after one hour, and the cluster is not destroyed. To resolve this issue, complete the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Manually ensure that there are no orphaned resources on your cloud, and that all of the provider resources that are associated with the managed cluster are cleaned up.

2.  Open the `ClusterDeployment` information for the managed cluster that is being removed by entering the following command:

    ``` bash
    oc edit clusterdeployment/<mycluster> -n <namespace>
    ```

    - Replace `mycluster` with the name of the managed cluster that you are destroying.

    - Replace `namespace` with the namespace of the managed cluster.

3.  Remove the `hive.openshift.io/deprovision` finalizer to forcefully stop the process that is trying to clean up the cluster resources in the cloud.

4.  Save your changes and verify that `ClusterDeployment` is gone.

5.  Manually remove the namespace of the managed cluster by running the following command:

    ``` bash
    oc delete ns <namespace>
    ```

    - Replace `namespace` with the namespace of the managed cluster.

</div>

<div>

<div class="title">

Additional resources

</div>

- [GH-4748](https://github.com/stolostron/backlog/issues/4748)

</div>

<a id="cannot-update-osd-console"></a>

### Cannot update OpenShift Container Platform Dedicated managed clusters with the console

You cannot use the Red Hat Advanced Cluster Management console to upgrade OpenShift Container Platform managed clusters that are in the OpenShift Container Platform Dedicated environment.

<div>

<div class="title">

Additional resources

</div>

- [GH-8922](https://github.com/stolostron/backlog/issues/8922)

</div>

<a id="non-ocp-pod-logs"></a>

### Non-OpenShift Container Platform managed clusters require *ManagedServiceAccount* or *LoadBalancer* for pod logs

The `ManagedServiceAccount` and cluster proxy add-ons are enabled by default in Red Hat Advanced Cluster Management version 2.10 and newer. If the add-ons are disabled after upgrading, you must enable the `ManagedServiceAccount` and cluster proxy add-ons manually to use the pod log feature.

<div>

<div class="title">

Procedure

</div>

1.  See *ManagedServiceAccount add-on* in [Advanced configuration](clusters.md#advanced-config-engine) to enable the `ManagedServiceAccount`.

2.  See [Configure proxy settings for cluster proxy add-ons](clusters.md#cluster-proxy-addon-settings) to enable a cluster proxy add-on.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-11034](https://issues.redhat.com/browse/ACM-11034)

</div>

<a id="cannot-reach-ipxe-script"></a>

### Client cannot reach iPXE script

iPXE is an open source network boot firmware. See [iPXE](https://ipxe.org/) for more details.

When booting a node, the URL length limitation in some DHCP servers cuts off the `ipxeScript` URL in the `InfraEnv` custom resource definition, resulting in the following error message in the console:

`no bootable devices`

To work around the issue, complete the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Apply the `InfraEnv` custom resource definition when using an assisted installation to expose the `bootArtifacts`, which might resemble the following file:

    ``` yaml
    status:
      agentLabelSelector:
        matchLabels:
          infraenvs.agent-install.openshift.io: qe2
      bootArtifacts:
        initrd: https://assisted-image-service-multicluster-engine.redhat.com/images/0000/pxe-initrd?api_key=0000000&arch=x86_64&version=4.11
        ipxeScript: https://assisted-service-multicluster-engine.redhat.com/api/assisted-install/v2/infra-envs/00000/downloads/files?api_key=000000000&file_name=ipxe-script
        kernel: https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/4.12/latest/rhcos-live-kernel-x86_64
        rootfs: https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/4.12/latest/rhcos-live-rootfs.x86_64.img
    ```

2.  Create a proxy server to expose the `bootArtifacts` with short URLs.

3.  Copy the `bootArtifacts` and add them to the proxy by running the following commands:

    ``` bash
    for artifact in oc get infraenv qe2 -ojsonpath="{.status.bootArtifacts}" | jq ". | keys[]" | sed "s/\"//g"
    do curl -k oc get infraenv qe2 -ojsonpath="{.status.bootArtifacts.${artifact}}"` -o $artifact
    ```

4.  Add the `ipxeScript` artifact proxy URL to the `bootp` parameter in `libvirt.xml`.

</div>

<div>

<div class="title">

Additional resources

</div>

- [GH-25157](https://github.com/stolostron/backlog/issues/25157)

</div>

<a id="managedclusterset-api-limitation"></a>

### ManagedClusterSet API specification limitation

The `selectorType: LaberSelector` setting is not supported when using the Clustersets API. The `selectorType: ExclusiveClusterSetLabel` setting is supported. Use the *API Explorer* in the console, or an `oc` command, to view current and supported APIs.

<div>

<div class="title">

Additional resources

</div>

- [ACM-6423](https://issues.redhat.com/browse/ACM-6423)

</div>

<a id="clustercurator-osd-unsupported"></a>

### Cluster curator does not support OpenShift Container Platform Dedicated clusters

When you upgrade an OpenShift Container Platform Dedicated cluster by using the `ClusterCurator` resource, the upgrade fails because the Cluster curator does not support OpenShift Container Platform Dedicated clusters.

<div>

<div class="title">

Additional resources

</div>

- [ACM-10154](https://issues.redhat.com/browse/ACM-10154)

</div>

<a id="custom-ingress-domain"></a>

### Custom ingress domain not applied correctly

You can specify a custom ingress domain by using the `ClusterDeployment` resource while installing a managed cluster, but the change is only applied after the installation by using the `SyncSet` resource. As a result, the `spec` field in the `clusterdeployment.yaml` file displays the custom ingress domain you specified, but the `status` still displays the default domain.

<div>

<div class="title">

Additional resources

</div>

- [ACM-6279](https://issues.redhat.com/browse/ACM-6279)

</div>

<a id="settings-limit-msa-agent"></a>

### *tolerations* and *nodeSelector* settings do not affect the *managed-serviceaccount* agent

The `tolerations` and `nodeSelector` settings configured on the `MultiClusterEngine` and `MultiClusterHub` resources do not affect the `managed-serviceaccount` agent deployed on the local cluster.

The `managed-serviceaccount` add-on is not always required on the local cluster. If the `managed-serviceaccount` add-on is required, you can work around the issue by completing the following steps.

To learn more about how to use the `addonDeploymentConfig` custom resource to configure `tolerations` and `nodeSelector` for add-on, see [Set up the *AddOnDeploymentConfig* to configure klusterlet add-ons](add-ons.md#setting-addondeploymentconfig-klusterlet-addons).

<div>

<div class="title">

Procedure

</div>

1.  Create the `addonDeploymentConfig` custom resource.

2.  Set the `tolerations` and `nodeSelector` values for the local cluster and `managed-serviceaccount` agent.

3.  Update the `managed-serviceaccount` `ManagedClusterAddon` in the local cluster namespace to use the `addonDeploymentConfig` custom resource you created.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-7523](https://issues.redhat.com/browse/ACM-7523)

</div>

<a id="assisted-incorrect-cached-image"></a>

### Assisted Installer pulls incorrect cached image in disconnected environments

In a disconnected environment, Assisted Installer might pull an incorrect cached release image instead of the image from your disconnected registry. To work around the issue, prevent the `cluster-image-set-controller` from recreating the `ClusterImageSet` resources during deletion and delete the `ClusterImageSet` resources on the hub cluster to clear the hub cluster image cache. After you restart the installation, the image is pulled correctly from the disconnected registry.

<div>

<div class="title">

Procedure

</div>

1.  Create a `ConfigMap` that points the controller to a Git repository that does not exist. Run the following command:

    ``` bash
    oc create configmap cluster-image-set-git-repo -n multicluster-engine \
      --from-literal=gitRepoUrl=https://github.com/stolostron/does-not-exist.git \
      --from-literal=channel=fast \
      --dry-run=client -o yaml > cluster-image-set-git-repo-cm.yaml
    ```

2.  Apply the changes. Run the following command:

    ``` bash
    oc apply -f cluster-image-set-git-repo-cm.yaml
    ```

3.  Delete the `ClusterImageSet` resources on the hub cluster to clear the hub cluster image cache. Run the following command:

    ``` bash
    oc delete clusterimagesets --all --ignore-not-found=true --wait=true --timeout=5m
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-29986](https://issues.redhat.com/browse/ACM-29986)

</div>

<a id="install-sno-ocp-infra"></a>

### single-node OpenShift cluster installation requires matching OpenShift Container Platform with infrastructure operator for Red Hat OpenShift

If you want to install a single-node OpenShift cluster with an Red Hat OpenShift Container Platform version before 4.19, your `InfraEnv` custom resource and your booted host must use the same OpenShift Container Platform version that you are using to install the single-node OpenShift cluster. The installation fails if the versions do not match.

<div>

<div class="title">

Procedure

</div>

1.  Edit your `InfraEnv` resource before you boot a host with the Discovery ISO, and include the following content.

    ``` yaml
    apiVersion: agent-install.openshift.io/v1beta1
    kind: InfraEnv
    spec:
      osImageVersion: "<4.x>"
    ```

2.  Replace `<4.x>` with the `osImageVersion` that you want to install.

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-14943](https://issues.redhat.com/browse/ACM-14943)

</div>

<a id="boot-discovery-auto-add-host"></a>

### Cannot use host inventory to boot with the discovery image and add hosts automatically

You cannot use a host inventory, or `InfraEnv` custom resource, to both boot with the discovery image and add hosts automatically. If you used your previous `InfraEnv` resource for the `BareMetalHost` resource, and you want to boot the image yourself, you can work around the issue by creating a new `InfraEnv` resource.

<div>

<div class="title">

Additional resources

</div>

- [ACM-14719](https://issues.redhat.com/browse/ACM-14719)

</div>

<a id="nodes-shut-down-bmh"></a>

### Nodes shut down after removing `BareMetalHost` resource

If you remove the `BareMetalHost` resource from a hub cluster, the nodes shut down. You can manually power on the nodes again.

<div>

<div class="title">

Additional resources

</div>

- [ACM-15319](https://issues.redhat.com/browse/ACM-15319)

</div>

<a id="stale-neighbor-cache-rejoin"></a>

### Managed cluster fails to rejoin hub cluster after Image-Based Break/Fix server replacement

After a bare-metal server is replaced by using Image-Based Break/Fix, or the cluster reinstallation feature of the SiteConfig operator, the managed cluster might fail to rejoin the hub cluster.

This issue occurs because the hub cluster node that hosts the API VIP retains a stale neighbor cache entry that maps the managed cluster IP address to the MAC address of the previous server.

The replacement server uses the same IP address, but has a different MAC address, which causes the hub cluster to send reply packets to the wrong Layer 2 address.

The klusterlet agent on the managed cluster display logs repeated timeout errors similar to the following message:

\+

``` bash
dial tcp <hub-api-address>:6443: i/o timeout
```

The SiteConfig operator reimport process loops indefinitely because the managed cluster never becomes healthy. To work around this issue, flush the stale neighbor cache entry on the hub cluster node that hosts the API VIP. Complete the following steps:

<div>

<div class="title">

Procedure

</div>

1.  Identify the hub cluster node that is running the API VIP.

2.  Verify that a stale neighbor cache entry exists on the hub cluster node by running the following command. Replace `<spoke-ip-address>` with the IP address of the managed cluster and `<bridge-interface>` with the network bridge interface name on the hub cluster node:

    ``` bash
    sudo ip neigh show to <spoke-ip-address> dev <bridge-interface>
    ```

3.  Delete the stale neighbor cache entry by running the following command:

    ``` bash
    sudo ip neigh del <spoke-ip-address> dev <bridge-interface>
    ```

4.  Verify that the managed cluster status changes to `Available` by running the following command. Replace `<cluster-name>` with the name of your managed cluster:

    ``` bash
    oc get managedcluster <cluster-name>
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [ACM-30330](https://issues.redhat.com/browse/ACM-30330)

</div>

<a id="deprecations-removals-cluster-mce"></a>

## Deprecations and removals for Cluster lifecycle with multicluster engine operator

Learn when parts of the product are deprecated or removed from multicluster engine operator. Consider the alternative actions in the *Recommended action* and details, which display in the tables for the current release and for two prior releases. Tables are removed if no entries are added for that section this release. **Best practice:** Upgrade to the most recent version.

**Deprecated:** multicluster engine operator 2.5 and earlier versions are no longer supported. The documentation might remain available, but without any errata releases for fixed issues or other updates.

Deprecated items  
Components, features, or services are supported, but no longer recommended for use and might become obsolete in future releases. Consider the alternative actions in the *Recommended action* and details that are provided in the table.

Removed items  
Function that was deprecated in previous releases and is no longer available in the product. You must use alternatives for the removed function. Consider the alternative actions in the *Recommended action* and details that are provided in the following table:

| Product or category | Affected item | Version | Recommended action | More details and links |
|----|----|----|----|----|
| ManagedClusterAddon | The `installNamespace` field is deprecated in the `ManagedClusterAddon` spec. | 2.10 | Use the `AddonDeploymentConfig` field. | None |
| KlusterletConfig | The `hubKubeAPIServerProxyConfig` field is deprecated in the `KlusterletConfig` spec. | 2.7 | Use the `hubKubeAPIServerConfig.proxyURL` and `hubKubeAPIServerConfig.trustedCABundles` fields. | None |
| KlusterletConfig | The `hubKubeAPIServerURL` field is deprecated in the `KlusterletConfig` spec. | 2.7 | Use the `hubKubeAPIServerConfig.url` field. | None |
| KlusterletConfig | The `hubKubeAPIServerCABundle` field is deprecated in the `KlusterletConfig` spec | 2.7 | Use the `hubKubeAPIServerConfig.serverVerificationStrategy` and `hubKubeAPIServerConfig.trustedCABundles` fields. | None |

Table list of *deprecated* items for multicluster engine operator

| Product or category | Affected item | Version | Recommended action | More details and links |
|----|----|----|----|----|
| Cluster lifecycle | The `autoImportRetry` field in `auto-import-secret.yaml` | 2.9 | None | None |

Table list of *removed* items for multicluster engine operator
