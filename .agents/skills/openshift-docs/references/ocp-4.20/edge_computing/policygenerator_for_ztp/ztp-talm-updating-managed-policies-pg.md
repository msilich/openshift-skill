<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use the Topology Aware Lifecycle Manager (TALM) to manage the software lifecycle of managed clusters that you have deployed using GitOps Zero Touch Provisioning (ZTP) and Topology Aware Lifecycle Manager (TALM). TALM uses Red Hat Advanced Cluster Management (RHACM) PolicyGenerator policies to manage and control changes applied to target clusters.

# Setting up the disconnected environment

TALM can perform both platform and Operator updates.

You must mirror both the platform image and Operator images that you want to update to in your mirror registry before you can use TALM to update your disconnected clusters.

<div>

<div class="title">

Procedure

</div>

- For platform updates, you must perform the following steps:

  1.  Mirror the required OpenShift Container Platform image repository. Ensure that the required platform image is mirrored by following the "Mirroring the OpenShift Container Platform image repository" procedure linked in the Additional resources. Save the contents of the `imageContentSources` section in the `imageContentSources.yaml` file:

      The following is example output:

      ``` yaml
      imageContentSources:
       - mirrors:
         - mirror-ocp-registry.ibmcloud.io.cpak:5000/openshift-release-dev/openshift4
         source: quay.io/openshift-release-dev/ocp-release
       - mirrors:
         - mirror-ocp-registry.ibmcloud.io.cpak:5000/openshift-release-dev/openshift4
         source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
      ```

  2.  Save the image signature of the required platform image that was mirrored. You must add the image signature to the `PolicyGenerator` CR for platform updates. To get the image signature, perform the following steps:

      1.  Specify the required OpenShift Container Platform tag by running the following command:

          ``` terminal
          $ OCP_RELEASE_NUMBER=<release_version>
          ```

      2.  Specify the architecture of the cluster by running the following command:

          ``` terminal
          $ ARCHITECTURE=<cluster_architecture>
          ```

          - `<cluster_architecture>` specifies the architecture of the cluster, such as `x86_64`, `aarch64`, `s390x`, or `ppc64le`.

      3.  Get the release image digest from Quay by running the following command

          ``` terminal
          $ DIGEST="$(oc adm release info quay.io/openshift-release-dev/ocp-release:${OCP_RELEASE_NUMBER}-${ARCHITECTURE} | sed -n 's/Pull From: .*@//p')"
          ```

      4.  Set the digest algorithm by running the following command:

          ``` terminal
          $ DIGEST_ALGO="${DIGEST%%:*}"
          ```

      5.  Set the digest signature by running the following command:

          ``` terminal
          $ DIGEST_ENCODED="${DIGEST#*:}"
          ```

      6.  Get the image signature from the [mirror.openshift.com](https://mirror.openshift.com/pub/openshift-v4/signatures/openshift/release/) website by running the following command:

          ``` terminal
          $ SIGNATURE_BASE64=$(curl -s "https://mirror.openshift.com/pub/openshift-v4/signatures/openshift/release/${DIGEST_ALGO}=${DIGEST_ENCODED}/signature-1" | base64 -w0 && echo)
          ```

      7.  Save the image signature to the `checksum-<OCP_RELEASE_NUMBER>.yaml` file by running the following commands:

          ``` terminal
          $ cat >checksum-${OCP_RELEASE_NUMBER}.yaml <<EOF
          ```

          ``` terminal
          ${DIGEST_ALGO}-${DIGEST_ENCODED}: ${SIGNATURE_BASE64}
          EOF
          ```

  3.  Prepare the update graph. You have two options to prepare the update graph:

      1.  Use the OpenShift Update Service.

          For more information about how to set up the graph on the hub cluster, see [Deploy the operator for OpenShift Update Service](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.4/html/clusters/managing-your-clusters#deploy-the-operator-for-cincinnati) and [Build the graph data init container](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.4/html/clusters/managing-your-clusters#build-the-graph-data-init-container).

      2.  Make a local copy of the upstream graph. Host the update graph on an `http` or `https` server in the disconnected environment that has access to the managed cluster. To download the update graph, use the following command:

          ``` terminal
          $ curl -s https://api.openshift.com/api/upgrades_info/v1/graph?channel=stable-4.20 -o ~/upgrade-graph_stable-4.20
          ```

- For Operator updates, you must perform the following task:

  - Mirror the Operator catalogs. Ensure that the required Operator images are mirrored by following the procedure in the "Mirroring Operator catalogs for use with disconnected clusters" section.

</div>

<div>

<div class="title">

Additional resources

</div>

- [About the Topology Aware Lifecycle Manager](../cnf-talm-for-cluster-upgrades.md#cnf-about-topology-aware-lifecycle-manager-config_cnf-topology-aware-lifecycle-manager)

- [Upgrading GitOps ZTP](../ztp-updating-gitops.md#ztp-updating-gitops)

- [Mirroring the OpenShift Container Platform image repository](../../disconnected/installing-mirroring-installation-images.md#installation-mirror-repository_installing-mirroring-installation-images)

- [Mirroring Operator catalogs for use with disconnected clusters](../../disconnected/installing-mirroring-installation-images.md#olm-mirror-catalog_installing-mirroring-installation-images)

- [Preparing the disconnected environment](../ztp-preparing-the-hub-cluster.md#ztp-preparing-the-hub-cluster)

- [Understanding update channels and releases](../../updating/understanding_updates/understanding-update-channels-release.md#understanding-update-channels-releases)

</div>

# Performing a platform update with PolicyGenerator CRs

You can perform a platform update with the TALM.

<div>

<div class="title">

Prerequisites

</div>

- Install the Topology Aware Lifecycle Manager (TALM).

- Update GitOps Zero Touch Provisioning (ZTP) to the latest version.

- Provision one or more managed clusters with GitOps ZTP.

- Mirror the required image repository.

- Log in as a user with `cluster-admin` privileges.

- Create RHACM policies in the hub cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `PolicyGenerator` CR for the platform update:

    1.  Save the following `PolicyGenerator` CR in the `du-upgrade.yaml` file:

        The following example shows the `PolicyGenerator` CR for platform update:

        ``` yaml
        apiVersion: policy.open-cluster-management.io/v1
        kind: PolicyGenerator
        metadata:
            name: du-upgrade
        placementBindingDefaults:
            name: du-upgrade-placement-binding
        policyDefaults:
            namespace: ztp-group-du-sno
            placement:
                labelSelector:
                    matchExpressions:
                        - key: group-du-sno
                          operator: Exists
            remediationAction: inform
            severity: low
            namespaceSelector:
                exclude:
                    - kube-*
                include:
                    - '*'
            evaluationInterval:
                compliant: 10m
                noncompliant: 10s
        policies:
            - name: du-upgrade-platform-upgrade
              policyAnnotations:
                ran.openshift.io/ztp-deploy-wave: "100"
              manifests:
                - path: source-crs/ClusterVersion.yaml
                  patches:
                    - metadata:
                        name: version
                      spec:
                        channel: stable-4.20
                        desiredUpdate:
                            version: 4.20.4
                        upstream: http://upgrade.example.com/images/upgrade-graph_stable-4.20
                      status:
                        history:
                            - state: Completed
                              version: 4.20.4
            - name: du-upgrade-platform-upgrade-prep
              policyAnnotations:
                ran.openshift.io/ztp-deploy-wave: "1"
              manifests:
                - path: source-crs/ImageSignature.yaml
                - path: source-crs/DisconnectedICSP.yaml
                  patches:
                    - metadata:
                        name: disconnected-internal-icsp-for-ocp
                      spec:
                        repositoryDigestMirrors:
                            - mirrors:
                                - quay-intern.example.com/ocp4/openshift-release-dev
                              source: quay.io/openshift-release-dev/ocp-release
                            - mirrors:
                                - quay-intern.example.com/ocp4/openshift-release-dev
                              source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
        ```

        - `source-crs/ClusterVersion.yaml` - Shows the `ClusterVersion` CR to trigger the update. The `channel`, `upstream`, and `desiredVersion` fields are all required for image precaching.

        - `source-crs/ImageSignature.yaml` - Contains the image signature of the required release image. The image signature is used to verify the image before applying the platform update.

        - `repositoryDigestMirrors` - Shows the mirror repository that contains the required OpenShift Container Platform image. Get the mirrors from the `imageContentSources.yaml` file that you saved when following the procedures in the "Setting up the environment" section.

        The `PolicyGenerator` CR generates two policies:

        - The `du-upgrade-platform-upgrade-prep` policy does the preparation work for the platform update. It creates the `ConfigMap` CR for the required release image signature, creates the image content source of the mirrored release image repository, and updates the cluster version with the required update channel and the update graph reachable by the managed cluster in the disconnected environment.

        - The `du-upgrade-platform-upgrade` policy is used to perform platform upgrade.

    2.  Add the `du-upgrade.yaml` file contents to the `kustomization.yaml` file located in the GitOps ZTP Git repository for the `PolicyGenerator` CRs and push the changes to the Git repository.

        ArgoCD pulls the changes from the Git repository and generates the policies on the hub cluster.

    3.  Check the created policies by running the following command:

        ``` terminal
        $ oc get policies -A | grep platform-upgrade
        ```

2.  Create the `ClusterGroupUpdate` CR for the platform update with the `spec.enable` field set to `false`.

    1.  Save the content of the platform update `ClusterGroupUpdate` CR with the `du-upgrade-platform-upgrade-prep` and the `du-upgrade-platform-upgrade` policies and the target clusters to the `cgu-platform-upgrade.yml` file, as shown in the following example:

        ``` yaml
        apiVersion: ran.openshift.io/v1alpha1
        kind: ClusterGroupUpgrade
        metadata:
          name: cgu-platform-upgrade
          namespace: default
        spec:
          managedPolicies:
          - du-upgrade-platform-upgrade-prep
          - du-upgrade-platform-upgrade
          preCaching: false
          clusters:
          - spoke1
          remediationStrategy:
            maxConcurrency: 1
          enable: false
        ```

    2.  Apply the `ClusterGroupUpdate` CR to the hub cluster by running the following command:

        ``` terminal
        $ oc apply -f cgu-platform-upgrade.yml
        ```

3.  Optional: Precache the images for the platform update.

    1.  Enable precaching in the `ClusterGroupUpdate` CR by running the following command:

        ``` terminal
        $ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-platform-upgrade \
        --patch '{"spec":{"preCaching": true}}' --type=merge
        ```

    2.  Monitor the update process and wait for the pre-caching to complete. Check the status of pre-caching by running the following command on the hub cluster:

        ``` terminal
        $ oc get cgu cgu-platform-upgrade -o jsonpath='{.status.precaching.status}'
        ```

4.  Start the platform update:

    1.  Enable the `cgu-platform-upgrade` policy and disable pre-caching by running the following command:

        ``` terminal
        $ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-platform-upgrade \
        --patch '{"spec":{"enable":true, "preCaching": false}}' --type=merge
        ```

    2.  Monitor the process. Upon completion, ensure that the policy is compliant by running the following command:

        ``` terminal
        $ oc get policies --all-namespaces
        ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Preparing the disconnected environment](../ztp-preparing-the-hub-cluster.md#ztp-acm-adding-images-to-mirror-registry_ztp-preparing-the-hub-cluster)

</div>

# Performing an Operator update with PolicyGenerator CRs

You can perform an Operator update with the TALM.

<div>

<div class="title">

Prerequisites

</div>

- Install the Topology Aware Lifecycle Manager (TALM).

- Update GitOps Zero Touch Provisioning (ZTP) to the latest version.

- Provision one or more managed clusters with GitOps ZTP.

- Mirror the required index image, bundle images, and all Operator images referenced in the bundle images.

- Log in as a user with `cluster-admin` privileges.

- Create RHACM policies in the hub cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Update the `PolicyGenerator` CR for the Operator update.

    1.  Update the `du-upgrade` `PolicyGenerator` CR with the following additional contents in the `du-upgrade.yaml` file:

        ``` yaml
        apiVersion: policy.open-cluster-management.io/v1
        kind: PolicyGenerator
        metadata:
            name: du-upgrade
        placementBindingDefaults:
            name: du-upgrade-placement-binding
        policyDefaults:
            namespace: ztp-group-du-sno
            placement:
                labelSelector:
                    matchExpressions:
                        - key: group-du-sno
                          operator: Exists
            remediationAction: inform
            severity: low
            namespaceSelector:
                exclude:
                    - kube-*
                include:
                    - '*'
            evaluationInterval:
                compliant: 10m
                noncompliant: 10s
        policies:
            - name: du-upgrade-operator-catsrc-policy
              policyAnnotations:
                ran.openshift.io/ztp-deploy-wave: "1"
              manifests:
                - path: source-crs/DefaultCatsrc.yaml
                  patches:
                    - metadata:
                        name: redhat-operators-disconnected
                      spec:
                        displayName: Red Hat Operators Catalog
                        image: registry.example.com:5000/olm/redhat-operators-disconnected:v4.20
                        updateStrategy:
                            registryPoll:
                                interval: 1h
                      status:
                        connectionState:
                            lastObservedState: READY
        ```

        - `image` - Contains the required Operator images. If the index images are always pushed to the same image name and tag, this change is not needed.

        - `updateStrategy` - Sets how frequently the Operator Lifecycle Manager (OLM) polls the index image for new Operator versions with the `registryPoll.interval` field. This change is not needed if a new index image tag is always pushed for y-stream and z-stream Operator updates. The `registryPoll.interval` field can be set to a shorter interval to expedite the update, however shorter intervals increase computational load. To counteract this, you can restore `registryPoll.interval` to the default value once the update is complete.

        - `lastObservedState` - Displays the observed state of the catalog connection. The `READY` value ensures that the `CatalogSource` policy is ready, indicating that the index pod is pulled and is running. This way, TALM upgrades the Operators based on up-to-date policy compliance states.

    2.  This update generates one policy, `du-upgrade-operator-catsrc-policy`, to update the `redhat-operators-disconnected` catalog source with the new index images that contain the required Operators images.

        > [!NOTE]
        > If you want to use the image precaching for Operators and there are Operators from a different catalog source other than `redhat-operators-disconnected`, you must perform the following tasks:
        >
        > - Prepare a separate catalog source policy with the new index image or registry poll interval update for the different catalog source.
        >
        > - Prepare a separate subscription policy for the required Operators that are from the different catalog source.

        For example, the required SRIOV-FEC Operator is available in the `certified-operators` catalog source. To update the catalog source and the Operator subscription, add the following contents to generate two policies, `du-upgrade-fec-catsrc-policy` and `du-upgrade-subscriptions-fec-policy`:

        ``` yaml
        apiVersion: policy.open-cluster-management.io/v1
        kind: PolicyGenerator
        metadata:
            name: du-upgrade
        placementBindingDefaults:
            name: du-upgrade-placement-binding
        policyDefaults:
            namespace: ztp-group-du-sno
            placement:
                labelSelector:
                    matchExpressions:
                        - key: group-du-sno
                          operator: Exists
            remediationAction: inform
            severity: low
            namespaceSelector:
                exclude:
                    - kube-*
                include:
                    - '*'
            evaluationInterval:
                compliant: 10m
                noncompliant: 10s
        policies:
            - name: du-upgrade-fec-catsrc-policy
              policyAnnotations:
                ran.openshift.io/ztp-deploy-wave: "1"
              manifests:
                - path: source-crs/DefaultCatsrc.yaml
                  patches:
                    - metadata:
                        name: certified-operators
                      spec:
                        displayName: Intel SRIOV-FEC Operator
                        image: registry.example.com:5000/olm/far-edge-sriov-fec:v4.10
                        updateStrategy:
                            registryPoll:
                                interval: 10m
            - name: du-upgrade-subscriptions-fec-policy
              policyAnnotations:
                ran.openshift.io/ztp-deploy-wave: "2"
              manifests:
                - path: source-crs/AcceleratorsSubscription.yaml
                  patches:
                    - spec:
                        channel: stable
                        source: certified-operators
        ```

    3.  Remove the specified subscriptions channels in the common `PolicyGenerator` CR, if they exist. The default subscriptions channels from the GitOps ZTP image are used for the update.

        > [!NOTE]
        > The default channel for the Operators applied through GitOps ZTP 4.20 is `stable`, except for the `performance-addon-operator`. As of OpenShift Container Platform 4.11, the `performance-addon-operator` functionality was moved to the `node-tuning-operator`. For the 4.10 release, the default channel for PAO is `v4.10`. You can also specify the default channels in the common `PolicyGenerator` CR.

    4.  Push the `PolicyGenerator` CRs updates to the GitOps ZTP Git repository.

        ArgoCD pulls the changes from the Git repository and generates the policies on the hub cluster.

    5.  Check the created policies by running the following command:

        ``` terminal
        $ oc get policies -A | grep -E "catsrc-policy|subscription"
        ```

2.  Apply the required catalog source updates before starting the Operator update.

    1.  Save the content of the `ClusterGroupUpgrade` CR named `operator-upgrade-prep` with the catalog source policies and the target managed clusters to the `cgu-operator-upgrade-prep.yml` file:

        ``` yaml
        apiVersion: ran.openshift.io/v1alpha1
        kind: ClusterGroupUpgrade
        metadata:
          name: cgu-operator-upgrade-prep
          namespace: default
        spec:
          clusters:
          - spoke1
          enable: true
          managedPolicies:
          - du-upgrade-operator-catsrc-policy
          remediationStrategy:
            maxConcurrency: 1
        ```

    2.  Apply the policy to the hub cluster by running the following command:

        ``` terminal
        $ oc apply -f cgu-operator-upgrade-prep.yml
        ```

    3.  Monitor the update process. Upon completion, ensure that the policy is compliant by running the following command:

        ``` terminal
        $ oc get policies -A | grep -E "catsrc-policy"
        ```

3.  Create the `ClusterGroupUpgrade` CR for the Operator update with the `spec.enable` field set to `false`.

    1.  Save the content of the Operator update `ClusterGroupUpgrade` CR with the `du-upgrade-operator-catsrc-policy` policy and the subscription policies created from the common `PolicyGenerator` and the target clusters to the `cgu-operator-upgrade.yml` file, as shown in the following example:

        ``` yaml
        apiVersion: ran.openshift.io/v1alpha1
        kind: ClusterGroupUpgrade
        metadata:
          name: cgu-operator-upgrade
          namespace: default
        spec:
          managedPolicies:
          - du-upgrade-operator-catsrc-policy
          - common-subscriptions-policy
          preCaching: false
          clusters:
          - spoke1
          remediationStrategy:
            maxConcurrency: 1
          enable: false
        ```

        - `du-upgrade-operator-catsrc-policy` is needed by the image precaching feature to retrieve the Operator images from the catalog source.

        - `common-subscriptions-policy` contains Operator subscriptions. If you have followed the structure and content of the reference `PolicyGenTemplates`, all Operator subscriptions are grouped into the `common-subscriptions-policy` policy.

        > [!NOTE]
        > One `ClusterGroupUpgrade` CR can only precache the images of the required Operators defined in the subscription policy from one catalog source included in the `ClusterGroupUpgrade` CR. If the required Operators are from different catalog sources, such as in the example of the SRIOV-FEC Operator, another `ClusterGroupUpgrade` CR must be created with `du-upgrade-fec-catsrc-policy` and `du-upgrade-subscriptions-fec-policy` policies for the SRIOV-FEC Operator images precaching and update.

    2.  Apply the `ClusterGroupUpgrade` CR to the hub cluster by running the following command:

        ``` terminal
        $ oc apply -f cgu-operator-upgrade.yml
        ```

4.  Optional: Precache the images for the Operator update.

    1.  Before starting image precaching, verify the subscription policy is `NonCompliant` at this point by running the following command:

        ``` terminal
        $ oc get policy common-subscriptions-policy -n <policy_namespace>
        ```

        The following is example output:

        ``` terminal
        NAME                          REMEDIATION ACTION   COMPLIANCE STATE     AGE
        common-subscriptions-policy   inform               NonCompliant         27d
        ```

    2.  Enable precaching in the `ClusterGroupUpgrade` CR by running the following command:

        ``` terminal
        $ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-operator-upgrade \
        --patch '{"spec":{"preCaching": true}}' --type=merge
        ```

    3.  Monitor the process and wait for the precaching to complete. Check the status of precaching by running the following command on the managed cluster:

        ``` terminal
        $ oc get cgu cgu-operator-upgrade -o jsonpath='{.status.precaching.status}'
        ```

    4.  Check if the precaching is completed before starting the update by running the following command:

        ``` terminal
        $ oc get cgu -n default cgu-operator-upgrade -ojsonpath='{.status.conditions}' | jq
        ```

        The following is example output:

        ``` json
        [
            {
              "lastTransitionTime": "2022-03-08T20:49:08.000Z",
              "message": "The ClusterGroupUpgrade CR is not enabled",
              "reason": "UpgradeNotStarted",
              "status": "False",
              "type": "Ready"
            },
            {
              "lastTransitionTime": "2022-03-08T20:55:30.000Z",
              "message": "Precaching is completed",
              "reason": "PrecachingCompleted",
              "status": "True",
              "type": "PrecachingDone"
            }
        ]
        ```

5.  Start the Operator update.

    1.  Enable the `cgu-operator-upgrade` `ClusterGroupUpgrade` CR and disable precaching to start the Operator update by running the following command:

        ``` terminal
        $ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-operator-upgrade \
        --patch '{"spec":{"enable":true, "preCaching": false}}' --type=merge
        ```

    2.  Monitor the process. Upon completion, ensure that the policy is compliant by running the following command:

        ``` terminal
        $ oc get policies --all-namespaces
        ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Upgrading GitOps ZTP](../ztp-updating-gitops.md#ztp-updating-gitops)

</div>

# Troubleshooting missed Operator updates with PolicyGenerator CRs

In some scenarios, Topology Aware Lifecycle Manager (TALM) might miss Operator updates due to an out-of-date policy compliance state.

After a catalog source update, it takes time for the Operator Lifecycle Manager (OLM) to update the subscription status. The status of the subscription policy might continue to show as compliant while TALM decides whether remediation is needed. As a result, the Operator specified in the subscription policy does not get upgraded.

To avoid this scenario, add another catalog source configuration to the `PolicyGenerator` and specify this configuration in the subscription for any Operators that require an update.

<div>

<div class="title">

Procedure

</div>

1.  Add a catalog source configuration in the `PolicyGenerator` resource:

    ``` yaml
    manifests:
    - path: source-crs/DefaultCatsrc.yaml
      patches:
        - metadata:
            name: redhat-operators-disconnected
          spec:
            displayName: Red Hat Operators Catalog
            image: registry.example.com:5000/olm/redhat-operators-disconnected:v{product-version}
            updateStrategy:
                registryPoll:
                    interval: 1h
          status:
            connectionState:
                lastObservedState: READY
    - path: source-crs/DefaultCatsrc.yaml
      patches:
        - metadata:
            name: redhat-operators-disconnected-v2
          spec:
            displayName: Red Hat Operators Catalog v2
            image: registry.example.com:5000/olm/redhat-operators-disconnected:<version>
            updateStrategy:
                registryPoll:
                    interval: 1h
          status:
            connectionState:
                lastObservedState: READY
    ```

    - `name` - Update the name for the new configuration.

    - `displayName` - Update the display name for the new configuration.

    - `image` - Update the index image URL. This `policies.manifests.patches.spec.image` field overrides any configuration in the `DefaultCatsrc.yaml` file.

2.  Update the `Subscription` resource to point to the new configuration for Operators that require an update:

    ``` yaml
    apiVersion: operators.coreos.com/v1alpha1
    kind: Subscription
    metadata:
      name: operator-subscription
      namespace: operator-namspace
    # ...
    spec:
      source: redhat-operators-disconnected-v2
    # ...
    ```

    - `redhat-operators-disconnected-v2` specifies the name of the additional catalog source configuration that you defined in the `PolicyGenerator` resource.

</div>

# Performing a platform and an Operator update together

You can perform a platform and an Operator update at the same time.

<div>

<div class="title">

Prerequisites

</div>

- Install the Topology Aware Lifecycle Manager (TALM).

- Update GitOps Zero Touch Provisioning (ZTP) to the latest version.

- Provision one or more managed clusters with GitOps ZTP.

- Log in as a user with `cluster-admin` privileges.

- Create RHACM policies in the hub cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `PolicyGenerator` CR for the updates by following the steps described in the "Performing a platform update" and "Performing an Operator update" sections.

2.  Apply the prep work for the platform and the Operator update.

    1.  Save the content of the `ClusterGroupUpgrade` CR with the policies for platform update preparation work, catalog source updates, and target clusters to the `cgu-platform-operator-upgrade-prep.yml` file, for example:

        ``` yaml
        apiVersion: ran.openshift.io/v1alpha1
        kind: ClusterGroupUpgrade
        metadata:
          name: cgu-platform-operator-upgrade-prep
          namespace: default
        spec:
          managedPolicies:
          - du-upgrade-platform-upgrade-prep
          - du-upgrade-operator-catsrc-policy
          clusterSelector:
          - group-du-sno
          remediationStrategy:
            maxConcurrency: 10
          enable: true
        ```

    2.  Apply the `cgu-platform-operator-upgrade-prep.yml` file to the hub cluster by running the following command:

        ``` terminal
        $ oc apply -f cgu-platform-operator-upgrade-prep.yml
        ```

    3.  Monitor the process. Upon completion, ensure that the policy is compliant by running the following command:

        ``` terminal
        $ oc get policies --all-namespaces
        ```

3.  Create the `ClusterGroupUpdate` CR for the platform and the Operator update with the `spec.enable` field set to `false`.

    1.  Save the contents of the platform and Operator update `ClusterGroupUpdate` CR with the policies and the target clusters to the `cgu-platform-operator-upgrade.yml` file, as shown in the following example:

        ``` yaml
        apiVersion: ran.openshift.io/v1alpha1
        kind: ClusterGroupUpgrade
        metadata:
          name: cgu-du-upgrade
          namespace: default
        spec:
          managedPolicies:
          - du-upgrade-platform-upgrade
          - du-upgrade-operator-catsrc-policy
          - common-subscriptions-policy
          preCaching: true
          clusterSelector:
          - group-du-sno
          remediationStrategy:
            maxConcurrency: 1
          enable: false
        ```

        - `du-upgrade-platform-upgrade` is the platform update policy.

        - `du-upgrade-operator-catsrc-policy` is the policy containing the catalog source information for the Operators to be updated. It is needed for the precaching feature to determine which Operator images to download to the managed cluster.

        - `common-subscriptions-policy` is the policy to update the Operators.

    2.  Apply the `cgu-platform-operator-upgrade.yml` file to the hub cluster by running the following command:

        ``` terminal
        $ oc apply -f cgu-platform-operator-upgrade.yml
        ```

4.  Optional: Precache the images for the platform and the Operator update.

    1.  Enable precaching in the `ClusterGroupUpgrade` CR by running the following command:

        ``` terminal
        $ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-du-upgrade \
        --patch '{"spec":{"preCaching": true}}' --type=merge
        ```

    2.  Monitor the update process and wait for the precaching to complete. Check the status of precaching by running the following command on the managed cluster:

        ``` terminal
        $ oc get jobs,pods -n openshift-talm-pre-cache
        ```

    3.  Check if the precaching is completed before starting the update by running the following command:

        ``` terminal
        $ oc get cgu cgu-du-upgrade -ojsonpath='{.status.conditions}'
        ```

5.  Start the platform and Operator update.

    1.  Enable the `cgu-du-upgrade` `ClusterGroupUpgrade` CR to start the platform and the Operator update by running the following command:

        ``` terminal
        $ oc --namespace=default patch clustergroupupgrade.ran.openshift.io/cgu-du-upgrade \
        --patch '{"spec":{"enable":true, "preCaching": false}}' --type=merge
        ```

    2.  Monitor the process. Upon completion, ensure that the policy is compliant by running the following command:

        ``` terminal
        $ oc get policies --all-namespaces
        ```

        > [!NOTE]
        > The CRs for the platform and Operator updates can be created from the beginning by configuring the setting to `spec.enable: true`. In this case, the update starts immediately after precaching completes and there is no need to manually enable the CR.
        >
        > Both precaching and the update create extra resources, such as policies, placement bindings, placement rules, managed cluster actions, and managed cluster view, to help complete the procedures. Setting the `afterCompletion.deleteObjects` field to `true` deletes all these resources after the updates complete.

</div>

# Removing Performance Addon Operator subscriptions from deployed clusters with PolicyGenerator CRs

In earlier versions of OpenShift Container Platform, the Performance Addon Operator provided automatic, low latency performance tuning for applications. In OpenShift Container Platform 4.11 or later, these functions are part of the Node Tuning Operator.

Do not install the Performance Addon Operator on clusters running OpenShift Container Platform 4.11 or later. If you upgrade to OpenShift Container Platform 4.11 or later, the Node Tuning Operator automatically removes the Performance Addon Operator.

> [!NOTE]
> You need to remove any policies that create Performance Addon Operator subscriptions to prevent a re-installation of the Operator.

The reference DU profile includes the Performance Addon Operator in the `PolicyGenerator` CR `acm-common-ranGen.yaml`. To remove the subscription from deployed managed clusters, you must update `acm-common-ranGen.yaml`.

> [!NOTE]
> If you install Performance Addon Operator 4.10.3-5 or later on OpenShift Container Platform 4.11 or later, the Performance Addon Operator detects the cluster version and automatically hibernates to avoid interfering with the Node Tuning Operator functions. However, to ensure best performance, remove the Performance Addon Operator from your OpenShift Container Platform 4.11 clusters.

<div>

<div class="title">

Prerequisites

</div>

- Create a Git repository where you manage your custom site configuration data. The repository must be accessible from the hub cluster and be defined as a source repository for ArgoCD.

- Update to OpenShift Container Platform 4.11 or later.

- Log in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Change the `complianceType` to `mustnothave` for the Performance Addon Operator namespace, Operator group, and subscription in the `acm-common-ranGen.yaml` file.

    ``` yaml
    - name: group-du-sno-pg-subscriptions-policy
      policyAnnotations:
        ran.openshift.io/ztp-deploy-wave: "2"
      manifests:
        - path: source-crs/PaoSubscriptionNS.yaml
        - path: source-crs/PaoSubscriptionOperGroup.yaml
        - path: source-crs/PaoSubscription.yaml
    ```

2.  Merge the changes with your custom site repository and wait for the ArgoCD application to synchronize the change to the hub cluster. The status of the `common-subscriptions-policy` policy changes to `Non-Compliant`.

3.  Apply the change to your target clusters by using the Topology Aware Lifecycle Manager. For more information about rolling out configuration changes, see the "Additional resources" section.

4.  Monitor the process. When the status of the `common-subscriptions-policy` policy for a target cluster is `Compliant`, the Performance Addon Operator has been removed from the cluster. Get the status of the `common-subscriptions-policy` by running the following command:

    ``` terminal
    $ oc get policy -n ztp-common common-subscriptions-policy
    ```

5.  Delete the Performance Addon Operator namespace, Operator group and subscription CRs from `policies.manifests` in the `acm-common-ranGen.yaml` file.

6.  Merge the changes with your custom site repository and wait for the ArgoCD application to synchronize the change to the hub cluster. The policy remains compliant.

</div>

# Precaching user-specified images with TALM on single-node OpenShift clusters

You can precache application-specific workload images on single-node OpenShift clusters before updating your applications.

You can specify the configuration options for the precaching jobs by using the following custom resources (CR):

- `PreCachingConfig` CR

- `ClusterGroupUpgrade` CR

TALM derives the platform image from the `ClusterVersion` object in the managed policies. TALM derives Operator index images from `CatalogSource` objects that the managed policies reference.

> [!NOTE]
> All fields in the `PreCachingConfig` CR are optional.

The following example shows a `PreCachingConfig` CR:

``` yaml
apiVersion: ran.openshift.io/v1alpha1
kind: PreCachingConfig
metadata:
  name: exampleconfig
  namespace: exampleconfig-ns
spec:
  overrides:
    operatorsPackagesAndChannels:
      - local-storage-operator: stable
      - ptp-operator: stable
      - sriov-network-operator: stable
  spaceRequired: 30 Gi
  excludePrecachePatterns:
    - aws
    - vsphere
  additionalImages:
    - quay.io/exampleconfig/application1@sha256:3d5800990dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47e2e1ef
    - quay.io/exampleconfig/application2@sha256:3d5800123dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47adfaef
    - quay.io/exampleconfig/applicationN@sha256:4fe1334adfafadsf987123adfffdaf1243340adfafdedga0991234afdadfsa09
```

- `overrides` - Specifies Operator packages and channels to precache instead of the values that TALM derives from the managed policies. The only supported override is `operatorsPackagesAndChannels`. TALM ignores the deprecated `platformImage` and `operatorsIndexes` override fields if they are present.

- `spaceRequired` - Specifies the minimum required disk space on the cluster. If unspecified, TALM defines a default value for OpenShift Container Platform images. The disk space field must include an integer value and the storage unit. For example: `40 GiB`, `200 MB`, `1 TiB`.

- `excludePrecachePatterns` - Specifies the images to exclude from precaching based on image name matching.

- `additionalImages` - Specifies the list of additional images to precache.

The following example shows a `ClusterGroupUpgrade` CR with a `PreCachingConfig` CR reference:

``` yaml
apiVersion: ran.openshift.io/v1alpha1
kind: ClusterGroupUpgrade
metadata:
  name: cgu
spec:
  preCaching: true
  preCachingConfigRef:
    name: exampleconfig
    namespace: exampleconfig-ns
```

- `preCaching` set to `true` enables the precaching job.

- `preCachingConfigRef.name` specifies the `PreCachingConfig` CR that you want to use.

- `preCachingConfigRef.namespace` specifies the namespace of the `PreCachingConfig` CR that you want to use.

## Creating the custom resources for precaching

You must create the `PreCachingConfig` CR before or concurrently with the `ClusterGroupUpgrade` CR.

<div>

<div class="title">

Procedure

</div>

1.  Create the `PreCachingConfig` CR with the list of additional images you want to precache.

    ``` yaml
    apiVersion: ran.openshift.io/v1alpha1
    kind: PreCachingConfig
    metadata:
      name: exampleconfig
      namespace: default
    spec:
    # ...
      spaceRequired: 30Gi
      additionalImages:
        - quay.io/exampleconfig/application1@sha256:3d5800990dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47e2e1ef
        - quay.io/exampleconfig/application2@sha256:3d5800123dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47adfaef
        - quay.io/exampleconfig/applicationN@sha256:4fe1334adfafadsf987123adfffdaf1243340adfafdedga0991234afdadfsa09
    ```

    - `namespace` must be accessible to the hub cluster.

    - `spaceRequired` - It is recommended to set the minimum disk space required field to ensure that there is sufficient storage space for the precached images.

2.  Create a `ClusterGroupUpgrade` CR with the `preCaching` field set to `true` and specify the `PreCachingConfig` CR created in the previous step:

    ``` yaml
    apiVersion: ran.openshift.io/v1alpha1
    kind: ClusterGroupUpgrade
    metadata:
      name: cgu
      namespace: default
    spec:
      clusters:
      - sno1
      - sno2
      preCaching: true
      preCachingConfigRef:
      - name: exampleconfig
        namespace: default
      managedPolicies:
        - du-upgrade-platform-upgrade
        - du-upgrade-operator-catsrc-policy
        - common-subscriptions-policy
      remediationStrategy:
        timeout: 240
    ```

    > [!WARNING]
    > Once you install the images on the cluster, you cannot change or delete them.

3.  When you want to start precaching the images, apply the `ClusterGroupUpgrade` CR by running the following command:

    ``` terminal
    $ oc apply -f cgu.yaml
    ```

    TALM verifies the `ClusterGroupUpgrade` CR. From this point, you can continue with the TALM precaching workflow.

    > [!NOTE]
    > All sites are precached concurrently.

</div>

<div>

<div class="title">

Verification

</div>

1.  Check the precaching status on the hub cluster where the `ClusterGroupUpgrade` CR is applied by running the following command:

    ``` terminal
    $ oc get cgu <cgu_name> -n <cgu_namespace> -oyaml
    ```

    The following example shows the derived precaching specification. The `platformImage` and `operatorsIndexes` values come from the managed policies, not from `PreCachingConfig` overrides.

    ``` yaml
      precaching:
        spec:
          platformImage: quay.io/openshift-release-dev/ocp-release@sha256:3d5800990dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47e2e1ef
          operatorsIndexes:
            - registry.example.com:5000/custom-redhat-operators:1.0.0
          operatorsPackagesAndChannels:
            - local-storage-operator: stable
            - ptp-operator: stable
            - sriov-network-operator: stable
          excludePrecachePatterns:
            - aws
            - vsphere
          additionalImages:
            - quay.io/exampleconfig/application1@sha256:3d5800990dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47e2e1ef
            - quay.io/exampleconfig/application2@sha256:3d5800123dee7cd4727d3fe238a97e2d2976d3808fc925ada29c559a47adfaef
            - quay.io/exampleconfig/applicationN@sha256:4fe1334adfafadsf987123adfffdaf1243340adfafdedga0991234afdadfsa09
          spaceRequired: "30"
        status:
          sno1: Starting
          sno2: Starting
    ```

    The precaching configurations are validated by checking if the managed policies exist. Valid configurations of the `ClusterGroupUpgrade` and the `PreCachingConfig` CRs result in the following statuses:

    The following example shows the output of valid CRs:

    ``` yaml
    - lastTransitionTime: "2023-01-01T00:00:01Z"
      message: All selected clusters are valid
      reason: ClusterSelectionCompleted
      status: "True"
      type: ClusterSelected
    - lastTransitionTime: "2023-01-01T00:00:02Z"
      message: Completed validation
      reason: ValidationCompleted
      status: "True"
      type: Validated
    - lastTransitionTime: "2023-01-01T00:00:03Z"
      message: Precaching spec is valid and consistent
      reason: PrecacheSpecIsWellFormed
      status: "True"
      type: PrecacheSpecValid
    - lastTransitionTime: "2023-01-01T00:00:04Z"
      message: Precaching in progress for 1 clusters
      reason: InProgress
      status: "False"
      type: PrecachingSucceeded
    ```

    The following example shows an invalid `PreCachingConfig` CR:

    ``` yaml
    Type:    "PrecacheSpecValid"
    Status:  False,
    Reason:  "PrecacheSpecIncomplete"
    Message: "Precaching spec is incomplete: failed to get PreCachingConfig resource due to PreCachingConfig.ran.openshift.io "<precaching_cr_name>" not found"
    ```

2.  You can find the precaching job by running the following command on the managed cluster:

    ``` terminal
    $ oc get jobs -n openshift-talo-pre-cache
    ```

    The following example shows a precaching job in progress:

    ``` terminal
    NAME        COMPLETIONS       DURATION      AGE
    pre-cache   0/1               1s            1s
    ```

3.  You can check the status of the pod created for the precaching job by running the following command:

    ``` terminal
    $ oc describe pod pre-cache -n openshift-talo-pre-cache
    ```

    The following example shows a precaching job in progress:

    ``` terminal
    Type        Reason              Age    From              Message
    Normal      SuccesfulCreate     19s    job-controller    Created pod: pre-cache-abcd1
    ```

4.  You can get live updates on the status of the job by running the following command:

    ``` terminal
    $ oc logs -f pre-cache-abcd1 -n openshift-talo-pre-cache
    ```

5.  To verify the precache job is successfully completed, run the following command:

    ``` terminal
    $ oc describe pod pre-cache -n openshift-talo-pre-cache
    ```

    The following example shows a completed precache job:

    ``` terminal
    Type        Reason              Age    From              Message
    Normal      SuccesfulCreate     5m19s  job-controller    Created pod: pre-cache-abcd1
    Normal      Completed           19s    job-controller    Job completed
    ```

6.  To verify that the images are successfully precached on the single-node OpenShift, do the following:

    1.  Enter into the node in debug mode:

        ``` terminal
        $ oc debug node/cnfdf00.example.lab
        ```

    2.  Change root to `host`:

        ``` terminal
        $ chroot /host/
        ```

    3.  Search for the required images:

        ``` terminal
        $ sudo podman images | grep <operator_name>
        ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Using the container image precache feature](../cnf-talm-for-cluster-upgrades.md#talo-precache-feature-concept_cnf-topology-aware-lifecycle-manager)

</div>

# About the auto-created ClusterGroupUpgrade CR for GitOps ZTP

TALM has a controller called `ManagedClusterForCGU` that monitors the `Ready` state of the `ManagedCluster` CRs on the hub cluster and creates the `ClusterGroupUpgrade` CRs for GitOps Zero Touch Provisioning (ZTP).

For any managed cluster in the `Ready` state without a `ztp-done` label applied, the `ManagedClusterForCGU` controller automatically creates a `ClusterGroupUpgrade` CR in the `ztp-install` namespace with its associated RHACM policies that are created during the GitOps ZTP process. TALM then remediates the set of configuration policies that are listed in the auto-created `ClusterGroupUpgrade` CR to push the configuration CRs to the managed cluster.

If there are no policies for the managed cluster at the time when the cluster becomes `Ready`, a `ClusterGroupUpgrade` CR with no policies is created. Upon completion of the `ClusterGroupUpgrade` the managed cluster is labeled as `ztp-done`. If there are policies that you want to apply for that managed cluster, manually create a `ClusterGroupUpgrade` as a Day 2 operation.

<div>

<div class="title">

Procedure

</div>

- View the auto-created `ClusterGroupUpgrade` CR for GitOps ZTP:

  The following example shows an auto-created `ClusterGroupUpgrade` CR for GitOps ZTP:

  ``` yaml
  apiVersion: ran.openshift.io/v1alpha1
  kind: ClusterGroupUpgrade
  metadata:
    generation: 1
    name: spoke1
    namespace: ztp-install
    ownerReferences:
    - apiVersion: cluster.open-cluster-management.io/v1
      blockOwnerDeletion: true
      controller: true
      kind: ManagedCluster
      name: spoke1
      uid: 98fdb9b2-51ee-4ee7-8f57-a84f7f35b9d5
    resourceVersion: "46666836"
    uid: b8be9cd2-764f-4a62-87d6-6b767852c7da
  spec:
    actions:
      afterCompletion:
        addClusterLabels:
          ztp-done: ""
        deleteClusterLabels:
          ztp-running: ""
        deleteObjects: true
      beforeEnable:
        addClusterLabels:
          ztp-running: ""
    clusters:
    - spoke1
    enable: true
    managedPolicies:
    - common-spoke1-config-policy
    - common-spoke1-subscriptions-policy
    - group-spoke1-config-policy
    - spoke1-config-policy
    - group-spoke1-validator-du-policy
    preCaching: false
    remediationStrategy:
      maxConcurrency: 1
      timeout: 240
  ```

  - `ztp-done: ""` is applied to the managed cluster when TALM completes the cluster configuration.

  - `ztp-running: ""` is applied to the managed cluster when TALM starts deploying the configuration policies.

</div>
