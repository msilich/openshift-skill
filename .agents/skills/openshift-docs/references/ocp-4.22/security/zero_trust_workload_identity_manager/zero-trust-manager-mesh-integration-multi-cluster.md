<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Configure SPIFFE Runtime Environment (SPIRE) federation across multiple OpenShift Container Platform clusters to enable cross-cluster mutual TLS (mTLS) authentication and zero trust workload identity in a multi-cluster service mesh deployment.

# Multi-cluster SPIFFE Runtime Environment integration with Red Hat OpenShift Service Mesh

Understand how SPIFFE Runtime Environment (SPIRE) federation integrates with multi-cluster Red Hat OpenShift Service Mesh. Cross-cluster mutual TLS (mTLS) lets workloads on separate clusters authenticate each other under a unified zero-trust identity framework.

Multi-cluster SPIRE integration extends single-cluster SPIRE capabilities to enable workloads in different clusters to authenticate each other using Secure Production Identity Framework for Everyone (SPIFFE) identities. This eliminates the need for separate certificate authorities per cluster and enables true cross-cluster zero-trust architecture.

## What gets federated

Federation happens at two layers, and both are required:

| Layer | What | How |
|----|----|----|
| SPIRE Federation | Trust bundles | SPIRE Servers exchange bundles via `https_spiffe` profile |
| Istio Federation | Service discovery and routing | `Istiod` discovers remote endpoints via remote secrets, routes traffic through east-west gateways |

# Preparing the environment for multi-cluster SPIFFE Runtime Environment federation

Export kubeconfig paths, trust domains, federation endpoints, and JWT issuer URLs for Cluster A and Cluster B before you deploy federated SPIFFE Runtime Environment (SPIRE) operands on both clusters.

<div>

<div class="title">

Prerequisites

</div>

- You have two OpenShift Container Platform clusters (4.x) with network connectivity between them.

- You have installed Zero Trust Workload Identity Manager on both clusters.

- The OpenShift CLI (`oc`) is configured with access to both clusters.

- You have installed the `istioctl` CLI tool.

- You have installed `helm`. This is used for gateway deployment.

- You have Istio version 1.29.2 or later.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Export the namespace variables by running the following commands:

    ``` terminal
    $ export ZTWIM_NS=zero-trust-workload-identity-manager
    ```

    ``` terminal
    $ export OSSM_NS=istio-system
    ```

    ``` terminal
    $ export OSSM_CNI=istio-cni
    ```

2.  Export the kubeconfig file paths for Cluster A and Cluster B by running the following commands:

    ``` terminal
    $ export CLUSTER_A_KUBECONFIG="/path/to/cluster-a/kubeconfig"
    ```

    ``` terminal
    $ export CLUSTER_B_KUBECONFIG="/path/to/cluster-b/kubeconfig"
    ```

3.  Set the base domain environment variables for Cluster A and Cluster B by running the following commands:

    ``` terminal
    $ export CLUSTER_A_BASE_DOMAIN=$(oc get ingresses.config/cluster \
      -o jsonpath='{.spec.domain}' --kubeconfig "${CLUSTER_A_KUBECONFIG}")
    ```

    ``` terminal
    $ export CLUSTER_B_BASE_DOMAIN=$(oc get ingresses.config/cluster \
      -o jsonpath='{.spec.domain}' --kubeconfig "${CLUSTER_B_KUBECONFIG}")
    ```

4.  Export the trust domain environment variables from the base domain of each cluster by running the following commands:

    ``` terminal
    $ export CLUSTER_A_TRUST_DOMAIN="${CLUSTER_A_BASE_DOMAIN}"
    ```

    ``` terminal
    $ export CLUSTER_B_TRUST_DOMAIN="${CLUSTER_B_BASE_DOMAIN}"
    ```

5.  Define the cluster and network environment variables by running the following commands:

    ``` terminal
    $ export CLUSTER_A=cluster-a
    ```

    ``` terminal
    $ export CLUSTER_B=cluster-b
    ```

    ``` terminal
    $ export NETWORK_A=network-a
    ```

    ``` terminal
    $ export NETWORK_B=network-b
    ```

6.  Export the federation endpoint URLs for Cluster A and Cluster B by running the following commands:

    ``` terminal
    $ export FEDERATION_ENDPOINT_A="https://federation.${CLUSTER_A_BASE_DOMAIN}"
    ```

    ``` terminal
    $ export FEDERATION_ENDPOINT_B="https://federation.${CLUSTER_B_BASE_DOMAIN}"
    ```

7.  Set the JWT issuer environment variables for Cluster A and Cluster B by running the following commands:

    ``` terminal
    $ export JWT_ISSUER_A="https://oidc-discovery.${CLUSTER_A_BASE_DOMAIN}"
    ```

    ``` terminal
    $ export JWT_ISSUER_B="https://oidc-discovery.${CLUSTER_B_BASE_DOMAIN}"
    ```

</div>

# Deploying SPIFFE Runtime Environment with federation on both clusters

Deploy SPIFFE Runtime Environment (SPIRE) operand custom resources (CRs) with federation enabled on Cluster A and Cluster B, wait for operands to become ready, and verify SDS configuration.

<div>

<div class="title">

Prerequisites

</div>

- You have completed preparing the environment for multi-cluster SPIRE federation. For more information, see "Preparing the environment for multi-cluster SPIFFE Runtime Environment federation".

- The environment variables from the "Preparing the environment for multi-cluster SPIFFE Runtime Environment federation" procedure are set.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Deploy SPIRE with federation enabled on Cluster A:

    1.  Create a YAML file that defines the `ZeroTrustWorkloadIdentityManager` CR on Cluster A:

        ``` yaml
        apiVersion: operator.openshift.io/v1alpha1
        kind: ZeroTrustWorkloadIdentityManager
        metadata:
          name: cluster
        spec:
          trustDomain: ${CLUSTER_A_TRUST_DOMAIN}
          clusterName: ${CLUSTER_A}
          bundleConfigMap: "spire-bundle"
        ```

    2.  Apply the YAML file on Cluster A by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_A_KUBECONFIG}" -f <filename>
        ```

    3.  Create a YAML file that defines the `SpireServer` CR on Cluster A:

        ``` yaml
        apiVersion: operator.openshift.io/v1alpha1
        kind: SpireServer
        metadata:
          name: cluster
        spec:
          logLevel: "info"
          logFormat: "text"
          jwtIssuer: $JWT_ISSUER_A
          caValidity: "24h"
          defaultX509Validity: "1h"
          defaultJWTValidity: "5m"
          caKeytype: "rsa-2048"
          jwtKeyType: "rsa-2048"
          keyManager: ""
          caSubject:
            country: "US"
            organization: "RH"
            commonName: "SPIRE Server CA"
          persistence:
            size: "5Gi"
            accessMode: "ReadWriteOnce"
          datastore:
            databaseType: "sqlite3"
            connectionString: "/run/spire/data/datastore.sqlite3"
            tlsSecretName: ""
            maxOpenConns: 100
            maxIdleConns: 10
            connMaxLifetime: 0
            disableMigration: "false"
          federation:
            bundleEndpoint:
              profile: "https_spiffe"
        ```

    4.  Apply the YAML file on Cluster A by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_A_KUBECONFIG}" -f <filename>
        ```

    5.  Create a YAML file that defines the `SpireAgent` CR on Cluster A:

        ``` yaml
        apiVersion: operator.openshift.io/v1alpha1
        kind: SpireAgent
        metadata:
          name: cluster
        spec:
          socketPath: "/run/spire/agent-sockets"
          logLevel: "info"
          logFormat: "text"
          nodeAttestor:
            k8sPSATEnabled: "true"
          workloadAttestors:
            k8sEnabled: "true"
            workloadAttestorsVerification:
              type: "auto"
              hostCertBasePath: "/etc/kubernetes"
              hostCertFileName: "kubelet-ca.crt"
            useNewContainerLocator: "true"
        ```

    6.  Apply the YAML file on Cluster A by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_A_KUBECONFIG}" -f <filename>
        ```

    7.  Create a YAML file that defines the `SpiffeCSIDriver` CR on Cluster A:

        ``` yaml
        apiVersion: operator.openshift.io/v1alpha1
        kind: SpiffeCSIDriver
        metadata:
          name: cluster
        spec:
          agentSocketPath: "/run/spire/agent-sockets"
          pluginName: csi.spiffe.io
        ```

    8.  Apply the YAML file on Cluster A by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_A_KUBECONFIG}" -f <filename>
        ```

    9.  Create a YAML file that defines the `SpireOIDCDiscoveryProvider` CR on Cluster A:

        ``` yaml
        apiVersion: operator.openshift.io/v1alpha1
        kind: SpireOIDCDiscoveryProvider
        metadata:
          name: cluster
        spec:
          logLevel: "info"
          logFormat: "text"
          csiDriverName: "csi.spiffe.io"
          jwtIssuer: $JWT_ISSUER_A
          replicaCount: 1
          managedRoute: "true"
        ```

    10. Apply the YAML file on Cluster A by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_A_KUBECONFIG}" -f <filename>
        ```

2.  Deploy SPIRE with federation enabled on Cluster B:

    1.  Create a YAML file that defines the `ZeroTrustWorkloadIdentityManager` CR on Cluster B:

        ``` yaml
        apiVersion: operator.openshift.io/v1alpha1
        kind: ZeroTrustWorkloadIdentityManager
        metadata:
          name: cluster
        spec:
          trustDomain: ${CLUSTER_B_TRUST_DOMAIN}
          clusterName: ${CLUSTER_B}
          bundleConfigMap: "spire-bundle"
        ```

    2.  Apply the YAML file on Cluster B by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_B_KUBECONFIG}" -f <filename>
        ```

    3.  Create a YAML file that defines the `SpireServer` CR on Cluster B:

        ``` yaml
        apiVersion: operator.openshift.io/v1alpha1
        kind: SpireServer
        metadata:
          name: cluster
        spec:
          logLevel: "info"
          logFormat: "text"
          jwtIssuer: $JWT_ISSUER_B
          caValidity: "24h"
          defaultX509Validity: "1h"
          defaultJWTValidity: "5m"
          caKeytype: "rsa-2048"
          jwtKeyType: "rsa-2048"
          keyManager: ""
          caSubject:
            country: "US"
            organization: "RH"
            commonName: "SPIRE Server CA"
          persistence:
            size: "5Gi"
            accessMode: "ReadWriteOnce"
          datastore:
            databaseType: "sqlite3"
            connectionString: "/run/spire/data/datastore.sqlite3"
            tlsSecretName: ""
            maxOpenConns: 100
            maxIdleConns: 10
            connMaxLifetime: 0
            disableMigration: "false"
          federation:
            bundleEndpoint:
              profile: "https_spiffe"
        ```

    4.  Apply the YAML file on Cluster B by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_B_KUBECONFIG}" -f <filename>
        ```

    5.  Create a YAML file that defines the `SpireAgent` CR on Cluster B:

        ``` yaml
        apiVersion: operator.openshift.io/v1alpha1
        kind: SpireAgent
        metadata:
          name: cluster
        spec:
          socketPath: "/run/spire/agent-sockets"
          logLevel: "info"
          logFormat: "text"
          nodeAttestor:
            k8sPSATEnabled: "true"
          workloadAttestors:
            k8sEnabled: "true"
            workloadAttestorsVerification:
              type: "auto"
              hostCertBasePath: "/etc/kubernetes"
              hostCertFileName: "kubelet-ca.crt"
            useNewContainerLocator: "true"
        ```

    6.  Apply the YAML file on Cluster B by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_B_KUBECONFIG}" -f <filename>
        ```

    7.  Create a YAML file that defines the `SpiffeCSIDriver` CR on Cluster B:

        ``` yaml
        apiVersion: operator.openshift.io/v1alpha1
        kind: SpiffeCSIDriver
        metadata:
          name: cluster
        spec:
          agentSocketPath: "/run/spire/agent-sockets"
          pluginName: csi.spiffe.io
        ```

    8.  Apply the YAML file on Cluster B by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_B_KUBECONFIG}" -f <filename>
        ```

    9.  Create a YAML file that defines the `SpireOIDCDiscoveryProvider` CR on Cluster B:

        ``` yaml
        apiVersion: operator.openshift.io/v1alpha1
        kind: SpireOIDCDiscoveryProvider
        metadata:
          name: cluster
        spec:
          logLevel: "info"
          logFormat: "text"
          csiDriverName: "csi.spiffe.io"
          jwtIssuer: $JWT_ISSUER_B
          replicaCount: 1
          managedRoute: "true"
        ```

    10. Apply the YAML file on Cluster B by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_B_KUBECONFIG}" -f <filename>
        ```

3.  Wait for the `spire-server` StatefulSet to become ready on Cluster A by running the following command:

    ``` terminal
    $ oc rollout status statefulset/spire-server --kubeconfig="${CLUSTER_A_KUBECONFIG}" -n ${ZTWIM_NS} --timeout=300s
    ```

4.  Wait for the `spire-agent` DaemonSet to become ready on Cluster A by running the following command:

    ``` terminal
    $ oc rollout status daemonset/spire-agent --kubeconfig="${CLUSTER_A_KUBECONFIG}" -n ${ZTWIM_NS} --timeout=300s
    ```

5.  Wait for the `spire-spiffe-csi-driver` DaemonSet to become ready on Cluster A by running the following command:

    ``` terminal
    $ oc rollout status daemonset/spire-spiffe-csi-driver --kubeconfig="${CLUSTER_A_KUBECONFIG}" -n ${ZTWIM_NS} --timeout=300s
    ```

6.  Wait for the `spire-spiffe-oidc-discovery-provider` deployment to become available on Cluster A by running the following command:

    ``` terminal
    $ oc wait --for=condition=Available deployment/spire-spiffe-oidc-discovery-provider \
      --kubeconfig="${CLUSTER_A_KUBECONFIG}" -n ${ZTWIM_NS} --timeout=300s
    ```

7.  Wait for the `spire-server` StatefulSet to become ready on Cluster B by running the following command:

    ``` terminal
    $ oc rollout status statefulset/spire-server --kubeconfig="${CLUSTER_B_KUBECONFIG}" -n ${ZTWIM_NS} --timeout=300s
    ```

8.  Wait for the `spire-agent` DaemonSet to become ready on Cluster B by running the following command:

    ``` terminal
    $ oc rollout status daemonset/spire-agent --kubeconfig="${CLUSTER_B_KUBECONFIG}" -n ${ZTWIM_NS} --timeout=300s
    ```

9.  Wait for the `spire-spiffe-csi-driver` DaemonSet to become ready on Cluster B by running the following command:

    ``` terminal
    $ oc rollout status daemonset/spire-spiffe-csi-driver --kubeconfig="${CLUSTER_B_KUBECONFIG}" -n ${ZTWIM_NS} --timeout=300s
    ```

10. Wait for the `spire-spiffe-oidc-discovery-provider` deployment to become available on Cluster B by running the following command:

    ``` terminal
    $ oc wait --for=condition=Available deployment/spire-spiffe-oidc-discovery-provider \
      --kubeconfig="${CLUSTER_B_KUBECONFIG}" -n ${ZTWIM_NS} --timeout=300s
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the SDS configuration is available on Cluster A by running the following command:

    ``` terminal
    $ oc get cm spire-agent --kubeconfig="${CLUSTER_A_KUBECONFIG}" -n "${ZTWIM_NS}" \
      -o jsonpath='{.data.agent\.conf}' | grep -A5 '"sds"'
    ```

2.  Verify that the SDS configuration is available on Cluster B by running the following command:

    ``` terminal
    $ oc get cm spire-agent --kubeconfig="${CLUSTER_B_KUBECONFIG}" -n "${ZTWIM_NS}" \
      -o jsonpath='{.data.agent\.conf}' | grep -A5 '"sds"'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    "sds": {
      "default_all_bundles_name": "ROOTCA",
      "default_bundle_name": "null"
    },
    ```

    </div>

</div>

# Additional resources

- [Installing the Zero Trust Workload Identity Manager](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html-single/security_and_compliance/index#zero-trust-manager-install)

- [Zero Trust Workload Identity Manager SPIRE federation](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/security_and_compliance/zero-trust-workload-identity-manager#zero-trust-manager-spire-federation_zero-trust-manager-oidc-federation)

# Configuring Red Hat OpenShift Service Mesh for multi-cluster SPIFFE Runtime Environment integration

Configure Red Hat OpenShift Service Mesh on each cluster with federation settings, east-west gateways, and remote secrets to enable cross-cluster service communication by using SPIRE-issued certificates.

<div>

<div class="title">

Prerequisites

</div>

- You deployed SPIFFE Runtime Environment (SPIRE) with federation for multi-cluster integration. For more information, see "Deploying SPIFFE Runtime Environment with federation on both clusters".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify that the federation routes are created on Cluster A by running the following command:

    ``` terminal
    $ oc get route -n ${ZTWIM_NS} --kubeconfig="${CLUSTER_A_KUBECONFIG}" | grep federation
    ```

2.  Verify that the federation routes are created on Cluster B by running the following command:

    ``` terminal
    $ oc get route -n ${ZTWIM_NS} --kubeconfig="${CLUSTER_B_KUBECONFIG}" | grep federation
    ```

3.  On Cluster A, create a `ClusterFederatedTrustDomain` object pointing to Cluster B by running the following command:

    1.  Create a YAML file that defines the `ClusterFederatedTrustDomain` CR on Cluster A:

        ``` yaml
        apiVersion: spire.spiffe.io/v1alpha1
        kind: ClusterFederatedTrustDomain
        metadata:
          name: federation-to-cluster-b
        spec:
          trustDomain: ${CLUSTER_B_TRUST_DOMAIN}
          bundleEndpointURL: ${FEDERATION_ENDPOINT_B}
          bundleEndpointProfile:
            type: https_spiffe
            endpointSPIFFEID: spiffe://${CLUSTER_B_TRUST_DOMAIN}/spire/server
        ```

    2.  Apply the YAML file on Cluster A by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_A_KUBECONFIG}" -f <filename>
        ```

4.  On Cluster B, create a `ClusterFederatedTrustDomain` object pointing to Cluster A by running the following command:

    1.  Create a YAML file that defines the `ClusterFederatedTrustDomain` CR on Cluster B:

        ``` yaml
        apiVersion: spire.spiffe.io/v1alpha1
        kind: ClusterFederatedTrustDomain
        metadata:
          name: federation-to-cluster-a
        spec:
          trustDomain: ${CLUSTER_A_TRUST_DOMAIN}
          bundleEndpointURL: ${FEDERATION_ENDPOINT_A}
          bundleEndpointProfile:
            type: https_spiffe
            endpointSPIFFEID: spiffe://${CLUSTER_A_TRUST_DOMAIN}/spire/server
        ```

    2.  Apply the YAML file on Cluster B by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_B_KUBECONFIG}" -f <filename>
        ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the SPIRE Server on Cluster A has the trust bundle from Cluster B by running the following command:

    ``` terminal
    $ oc exec --kubeconfig="${CLUSTER_A_KUBECONFIG}" -n ${ZTWIM_NS} spire-server-0 -c spire-server -- \
      spire-server bundle list -socketPath /tmp/spire-server/private/api.sock -format spiffe 2>&1 | head -5
    ```

    The output must show public keys for `${CLUSTER_B_TRUST_DOMAIN}`.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` text
    {
      "trust_domains": {
        "${CLUSTER_B_TRUST_DOMAIN}": {
          "keys": [
    ```

    </div>

2.  Verify that the SPIRE Server on Cluster B has the trust bundle from Cluster A by running the following command:

    ``` terminal
    $ oc exec --kubeconfig="${CLUSTER_B_KUBECONFIG}" -n ${ZTWIM_NS} spire-server-0 -c spire-server -- \
      spire-server bundle list -socketPath /tmp/spire-server/private/api.sock -format spiffe 2>&1 | head -5
    ```

    The output must show public keys for `${CLUSTER_A_TRUST_DOMAIN}`.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` text
    {
      "trust_domains": {
        "${CLUSTER_A_TRUST_DOMAIN}": {
          "keys": [
    ```

    </div>

3.  Verify that the federation endpoint on Cluster A is reachable by running the following command:

    ``` terminal
    $ curl -sk "${FEDERATION_ENDPOINT_A}" | python3 -c "import sys,json; print(f'Keys: {len(json.load(sys.stdin).get(\"keys\",[]))}')"
    ```

    The output must show at least one `x509-svid` key and one `jwt-svid` key.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` text
    Keys: 2
    ```

    </div>

4.  Verify that the federation endpoint on Cluster B is reachable by running the following command:

    ``` terminal
    $ curl -sk "${FEDERATION_ENDPOINT_B}" | python3 -c "import sys,json; print(f'Keys: {len(json.load(sys.stdin).get(\"keys\",[]))}')"
    ```

    The output must show at least one `x509-svid` key and one `jwt-svid` key.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` text
    Keys: 2
    ```

    </div>

</div>

# Deploying the Red Hat OpenShift Service Mesh CNI on both clusters

Deploy the `IstioCNI` CR and federated `ClusterSPIFFEID` resources on Cluster A and Cluster B. This configures Red Hat OpenShift Service Mesh CNI networking and federated SPIFFE trust for cross-cluster mesh workloads.

<div>

<div class="title">

Prerequisites

</div>

- You have configured Red Hat OpenShift Service Mesh for multi-cluster integration. For more information, see "Configuring Red Hat OpenShift Service Mesh for multi-cluster SPIFFE Runtime Environment integration".

- The environment variables from the "Preparing the environment for multi-cluster SPIFFE Runtime Environment federation" and "Deploying SPIFFE Runtime Environment with federation on both clusters" procedures are set.

- You have installed Red Hat OpenShift Service Mesh 2.6.11 on both clusters.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the Red Hat OpenShift Service Mesh CNI namespace on Cluster A by running the following command:

    ``` terminal
    $ oc new-project "${OSSM_CNI}" --kubeconfig="${CLUSTER_A_KUBECONFIG}" 2>/dev/null || true
    ```

2.  Deploy the `IstioCNI` CR on Cluster A by running the following command:

    1.  Create a YAML file that defines the `IstioCNI` CR on Cluster A:

        ``` yaml
        apiVersion: sailoperator.io/v1
        kind: IstioCNI
        metadata:
          name: default
        spec:
          namespace: ${OSSM_CNI}
        ```

    2.  Apply the YAML file on Cluster A by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_A_KUBECONFIG}" -f <filename>
        ```

3.  Wait for the `istio-cni-node` DaemonSet to be created on Cluster A by running the following command:

    ``` terminal
    $ until oc get daemonset/istio-cni-node --kubeconfig="${CLUSTER_A_KUBECONFIG}" -n "${OSSM_CNI}" &> /dev/null; do
      sleep 3
    done
    ```

4.  Wait for the `IstioCNI` DaemonSet to become ready on Cluster A by running the following command:

    ``` terminal
    $ oc rollout status daemonset/istio-cni-node --kubeconfig="${CLUSTER_A_KUBECONFIG}" -n "${OSSM_CNI}" --timeout=300s
    ```

5.  Create the Red Hat OpenShift Service Mesh CNI namespace on Cluster B by running the following command:

    ``` terminal
    $ oc new-project "${OSSM_CNI}" --kubeconfig="${CLUSTER_B_KUBECONFIG}" 2>/dev/null || true
    ```

6.  Deploy the `IstioCNI` CR on Cluster B by running the following command:

    1.  Create a YAML file that defines the `IstioCNI` CR on Cluster B:

        ``` yaml
        apiVersion: sailoperator.io/v1
        kind: IstioCNI
        metadata:
          name: default
        spec:
          namespace: ${OSSM_CNI}
        ```

    2.  Apply the YAML file on Cluster B by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_B_KUBECONFIG}" -f <filename>
        ```

7.  Wait for the `istio-cni-node` DaemonSet to be created on Cluster B by running the following command:

    ``` terminal
    $ until oc get daemonset/istio-cni-node --kubeconfig="${CLUSTER_B_KUBECONFIG}" -n "${OSSM_CNI}" &> /dev/null; do
      sleep 3
    done
    ```

8.  Wait for the `IstioCNI` DaemonSet to become ready on Cluster B by running the following command:

    ``` terminal
    $ oc rollout status daemonset/istio-cni-node --kubeconfig="${CLUSTER_B_KUBECONFIG}" -n "${OSSM_CNI}" --timeout=300s
    ```

9.  Create the federated `ClusterSPIFFEID` resources on Cluster A by running the following command:

    1.  Create a YAML file that defines the federated `ClusterSPIFFEID` resources on Cluster A:

        ``` yaml
        apiVersion: spire.spiffe.io/v1alpha1
        kind: ClusterSPIFFEID
        metadata:
          name: sample-federation
        spec:
          className: zero-trust-workload-identity-manager-spire
          spiffeIDTemplate: "spiffe://{{ .TrustDomain }}/ns/{{ .PodMeta.Namespace }}/sa/{{ .PodSpec.ServiceAccountName }}"
          namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: sample
          federatesWith:
            - "${CLUSTER_B_TRUST_DOMAIN}"
        ---
        apiVersion: spire.spiffe.io/v1alpha1
        kind: ClusterSPIFFEID
        metadata:
          name: istio-system-federation
        spec:
          className: zero-trust-workload-identity-manager-spire
          spiffeIDTemplate: "spiffe://{{ .TrustDomain }}/ns/{{ .PodMeta.Namespace }}/sa/{{ .PodSpec.ServiceAccountName }}"
          namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: istio-system
          federatesWith:
            - "${CLUSTER_B_TRUST_DOMAIN}"
        ```

    2.  Apply the YAML file on Cluster A by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_A_KUBECONFIG}" -f <filename>
        ```

10. Create federated `ClusterSPIFFEID` resources on Cluster B by running the following command:

    1.  Create a YAML file that defines the federated `ClusterSPIFFEID` resources on Cluster B:

        ``` yaml
        apiVersion: spire.spiffe.io/v1alpha1
        kind: ClusterSPIFFEID
        metadata:
          name: sample-federation
        spec:
          className: zero-trust-workload-identity-manager-spire
          spiffeIDTemplate: "spiffe://{{ .TrustDomain }}/ns/{{ .PodMeta.Namespace }}/sa/{{ .PodSpec.ServiceAccountName }}"
          namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: sample
          federatesWith:
            - "${CLUSTER_A_TRUST_DOMAIN}"
        ---
        apiVersion: spire.spiffe.io/v1alpha1
        kind: ClusterSPIFFEID
        metadata:
          name: istio-system-federation
        spec:
          className: zero-trust-workload-identity-manager-spire
          spiffeIDTemplate: "spiffe://{{ .TrustDomain }}/ns/{{ .PodMeta.Namespace }}/sa/{{ .PodSpec.ServiceAccountName }}"
          namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: istio-system
          federatesWith:
            - "${CLUSTER_A_TRUST_DOMAIN}"
        ```

    2.  Apply the YAML file on Cluster B by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_B_KUBECONFIG}" -f <filename>
        ```

        > [!IMPORTANT]
        > Do not patch the default `ClusterSPIFFEID` (`zero-trust-workload-identity-manager-spire-default`). The Zero Trust Workload Identity Manager reconciles and reverts manual changes. Instead, create custom `ClusterSPIFFEID` resources for the specific namespaces.

</div>

# Deploying the Istio custom resource with the federation configuration

Deploy the Istio custom resource on Cluster A and Cluster B with SPIFFE Runtime Environment (SPIRE) federation and multi-cluster Red Hat OpenShift Service Mesh settings. This configures Istiod to obtain workload certificates from SPIRE and to trust SPIFFE bundles from both clusters for cross-cluster mTLS.

The Istio CR must include the following fields and values:

- A `meshConfig.trustDomain` value that matches the SPIRE trust domain.

- A `meshConfig.caCertificates` value with bundle URLs for both clusters. This handles cross-trust-domain validation.

- A `WORKLOAD_IDENTITY_SOCKET_FILE` value for SPIRE SDS integration.

- A `jwksResolverExtraRootCA` value for OIDC validation.

- A multi-cluster configuration that includes `meshID`, `clusterName`, and `network`.

- A SPIRE injection template configuration.

> [!NOTE]
> Do not use `meshConfig.trustDomainAliases`. Use `meshConfig.caCertificates` with `spiffeBundleUrl` instead.

<div>

<div class="title">

Prerequisites

</div>

- You have completed deploying the Istio Container Network Interface (CNI) on both clusters. For more information, see "Deploying Red Hat OpenShift Service Mesh CNI on both clusters".

- The environment variables from the "Preparing the environment for multi-cluster SPIFFE Runtime Environment federation" and "Deploying SPIFFE Runtime Environment with federation on both clusters" procedures are set.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Extract the OpenID Connect (OIDC) certificate on Cluster A by running the following command:

    ``` terminal
    $ export EXTRA_ROOT_CA_A="$(oc get secret oidc-serving-cert \
      --kubeconfig="${CLUSTER_A_KUBECONFIG}" -n ${ZTWIM_NS} -o json | \
      jq -r '.data."tls.crt"' | base64 -d | sed 's/^/        /')"
    ```

2.  Extract the OpenID Connect (OIDC) certificate on Cluster B by running the following command:

    ``` terminal
    $ export EXTRA_ROOT_CA_B="$(oc get secret oidc-serving-cert \
      --kubeconfig="${CLUSTER_B_KUBECONFIG}" -n ${ZTWIM_NS} -o json | \
      jq -r '.data."tls.crt"' | base64 -d | sed 's/^/        /')"
    ```

3.  Get the bundle endpoint URL for Cluster A by running the following command:

    ``` terminal
    $ export BUNDLE_URL_A="${FEDERATION_ENDPOINT_A}"
    ```

4.  Get the bundle endpoint URL for Cluster B by running the following command:

    ``` terminal
    $ export BUNDLE_URL_B="${FEDERATION_ENDPOINT_B}"
    ```

5.  Create the `Istio` custom resource (CR) on Cluster A by running the following command:

    ``` terminal
    $ oc new-project "${OSSM_NS}" --kubeconfig="${CLUSTER_A_KUBECONFIG}" 2>/dev/null || true
    ```

6.  Apply the `Istio` CR on Cluster A by running the following command:

    1.  Create a YAML file that defines the `Istio` CR on Cluster A:

        ``` yaml
        apiVersion: sailoperator.io/v1
        kind: Istio
        metadata:
          name: default
        spec:
          namespace: istio-system
          updateStrategy:
            type: InPlace
          values:
            meshConfig:
              trustDomain: ${CLUSTER_A_TRUST_DOMAIN}
              defaultConfig:
                proxyMetadata:
                  WORKLOAD_IDENTITY_SOCKET_FILE: "spire-agent.sock"
              caCertificates:
                - spiffeBundleUrl: ${BUNDLE_URL_A}
                  trustDomains:
                    - ${CLUSTER_A_TRUST_DOMAIN}
                - spiffeBundleUrl: ${BUNDLE_URL_B}
                  trustDomains:
                    - ${CLUSTER_B_TRUST_DOMAIN}
            global:
              meshID: mesh1
              multiCluster:
                clusterName: ${CLUSTER_A}
              network: ${NETWORK_A}
            pilot:
              jwksResolverExtraRootCA: |
                ${EXTRA_ROOT_CA_A}
              env:
                ENABLE_CA_SERVER: "true"
            sidecarInjectorWebhook:
              templates:
                spire: |
                  spec:
                    initContainers:
                    - name: istio-proxy
                      volumeMounts:
                      - name: workload-socket
                        mountPath: /run/secrets/workload-spiffe-uds
                        readOnly: true
                    volumes:
                      - name: workload-socket
                        csi:
                          driver: "csi.spiffe.io"
                          readOnly: true
                spireGw: |
                  spec:
                    containers:
                    - name: istio-proxy
                      volumeMounts:
                      - name: workload-socket
                        mountPath: /run/secrets/workload-spiffe-uds
                        readOnly: true
                    volumes:
                      - name: workload-socket
                        csi:
                          driver: "csi.spiffe.io"
                          readOnly: true
        ```

    2.  Apply the YAML file on Cluster A by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_A_KUBECONFIG}" -f <filename>
        ```

7.  Create the `Istio` CR on Cluster B by running the following command:

    ``` terminal
    $ oc new-project "${OSSM_NS}" --kubeconfig="${CLUSTER_B_KUBECONFIG}" 2>/dev/null || true
    ```

8.  Apply the `Istio` CR on Cluster B by running the following command:

    1.  Create a YAML file that defines the `Istio` CR on Cluster B:

        ``` yaml
        apiVersion: sailoperator.io/v1
        kind: Istio
        metadata:
          name: default
        spec:
          namespace: istio-system
          updateStrategy:
            type: InPlace
          values:
            meshConfig:
              trustDomain: ${CLUSTER_B_TRUST_DOMAIN}
              defaultConfig:
                proxyMetadata:
                  WORKLOAD_IDENTITY_SOCKET_FILE: "spire-agent.sock"
              caCertificates:
                - spiffeBundleUrl: ${BUNDLE_URL_B}
                  trustDomains:
                    - ${CLUSTER_B_TRUST_DOMAIN}
                - spiffeBundleUrl: ${BUNDLE_URL_A}
                  trustDomains:
                    - ${CLUSTER_A_TRUST_DOMAIN}
            global:
              meshID: mesh1
              multiCluster:
                clusterName: ${CLUSTER_B}
              network: ${NETWORK_B}
            pilot:
              jwksResolverExtraRootCA: |
                ${EXTRA_ROOT_CA_B}
              env:
                ENABLE_CA_SERVER: "true"
            sidecarInjectorWebhook:
              templates:
                spire: |
                  spec:
                    initContainers:
                    - name: istio-proxy
                      volumeMounts:
                      - name: workload-socket
                        mountPath: /run/secrets/workload-spiffe-uds
                        readOnly: true
                    volumes:
                      - name: workload-socket
                        csi:
                          driver: "csi.spiffe.io"
                          readOnly: true
                spireGw: |
                  spec:
                    containers:
                    - name: istio-proxy
                      volumeMounts:
                      - name: workload-socket
                        mountPath: /run/secrets/workload-spiffe-uds
                        readOnly: true
                    volumes:
                      - name: workload-socket
                        csi:
                          driver: "csi.spiffe.io"
                          readOnly: true
        ```

    2.  Apply the YAML file on Cluster B by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_B_KUBECONFIG}" -f <filename>
        ```

9.  Wait for the `istiod` deployment to be created on Cluster A by running the following command:

    ``` terminal
    $ until oc get deployment istiod --kubeconfig="${CLUSTER_A_KUBECONFIG}" -n "${OSSM_NS}" &> /dev/null; do
      sleep 3
    done
    ```

10. Wait for `Istiod` to become ready on Cluster A by running the following command:

    ``` terminal
    $ oc wait --for=condition=Available deployment/istiod \
      --kubeconfig="${CLUSTER_A_KUBECONFIG}" -n "${OSSM_NS}" --timeout=300s
    ```

11. Wait for the `istiod` deployment to be created on Cluster B by running the following command:

    ``` terminal
    $ until oc get deployment istiod --kubeconfig="${CLUSTER_B_KUBECONFIG}" -n "${OSSM_NS}" &> /dev/null; do
      sleep 3
    done
    ```

12. Wait for `Istiod` to become ready on Cluster B by running the following command:

    ``` terminal
    $ oc wait --for=condition=Available deployment/istiod \
      --kubeconfig="${CLUSTER_B_KUBECONFIG}" -n "${OSSM_NS}" --timeout=300s
    ```

</div>

# Verifying SPIRE integration with Istio on each cluster

Verify that Red Hat OpenShift Service Mesh on Cluster A and Cluster B obtains workload certificates from SPIFFE Runtime Environment (SPIRE). This confirms Istio sidecars use SPIRE-issued identities rather than the built-in Istio certificate authority (CA) before you proceed with cross-cluster mesh verification.

<div>

<div class="title">

Prerequisites

</div>

- You have deployed the Istio custom resource (CR) with the federation configuration. For more information, see "Deploying the Istio custom resource with the federation configuration".

- The environment variables from the "Preparing the environment for multi-cluster SPIFFE Runtime Environment federation" and "Deploying SPIFFE Runtime Environment with federation on both clusters" procedures are set.

- Istiod is running and ready on Cluster A and Cluster B.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set the verification namespace variable by running the following command:

    ``` terminal
    $ export VERIFY_NS=verify-ossm-ztwim
    ```

2.  Prepare the verification namespace on both clusters by running the following commands:

    1.  Create the verification namespace on Cluster A:

        ``` terminal
        $ oc create namespace ${VERIFY_NS} --kubeconfig="${CLUSTER_A_KUBECONFIG}" 2>/dev/null || true
        ```

    2.  Enable Istio injection for the verification namespace on Cluster A:

        ``` terminal
        $ oc label namespace ${VERIFY_NS} istio-injection=enabled \
          --kubeconfig="${CLUSTER_A_KUBECONFIG}" --overwrite
        ```

    3.  Create the verification namespace on Cluster B:

        ``` terminal
        $ oc create namespace ${VERIFY_NS} --kubeconfig="${CLUSTER_B_KUBECONFIG}" 2>/dev/null || true
        ```

    4.  Enable Istio injection for the verification namespace on Cluster B:

        ``` terminal
        $ oc label namespace ${VERIFY_NS} istio-injection=enabled \
          --kubeconfig="${CLUSTER_B_KUBECONFIG}" --overwrite
        ```

3.  Deploy the `httpbin` workload on Cluster A by running the following command:

    1.  Create a YAML file that defines the `httpbin` `Deployment` on Cluster A:

        ``` yaml
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: httpbin
          namespace: ${VERIFY_NS}
        spec:
          replicas: 1
          selector:
            matchLabels:
              app: httpbin
              version: v1
          template:
            metadata:
              annotations:
                inject.istio.io/templates: "sidecar,spire"
                spiffe.io/audience: "test-audience"
              labels:
                app: httpbin
                version: v1
            spec:
              containers:
              - image: docker.io/mccutchen/go-httpbin:v2.15.0
                imagePullPolicy: IfNotPresent
                name: httpbin
                ports:
                - containerPort: 8080
        ```

    2.  Apply the YAML file on Cluster A by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_A_KUBECONFIG}" -f <filename>
        ```

4.  Deploy the `httpbin` workload on Cluster B by running the following command:

    1.  Create a YAML file that defines the `httpbin` `Deployment` on Cluster B:

        ``` yaml
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: httpbin
          namespace: ${VERIFY_NS}
        spec:
          replicas: 1
          selector:
            matchLabels:
              app: httpbin
              version: v1
          template:
            metadata:
              annotations:
                inject.istio.io/templates: "sidecar,spire"
                spiffe.io/audience: "test-audience"
              labels:
                app: httpbin
                version: v1
            spec:
              containers:
              - image: docker.io/mccutchen/go-httpbin:v2.15.0
                imagePullPolicy: IfNotPresent
                name: httpbin
                ports:
                - containerPort: 8080
        ```

    2.  Apply the YAML file on Cluster B by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_B_KUBECONFIG}" -f <filename>
        ```

5.  Wait for the `httpbin` deployment to become available on Cluster A by running the following command:

    ``` terminal
    $ oc rollout status deployment/httpbin \
      -n "${VERIFY_NS}" --kubeconfig="${CLUSTER_A_KUBECONFIG}" --timeout=300s
    ```

6.  Wait for the `httpbin` deployment to become available on Cluster B by running the following command:

    ``` terminal
    $ oc rollout status deployment/httpbin \
      -n "${VERIFY_NS}" --kubeconfig="${CLUSTER_B_KUBECONFIG}" --timeout=300s
    ```

7.  Verify the Envoy sidecar certificate on Cluster A by running the following commands:

    1.  Get the `httpbin` pod name on Cluster A:

        ``` terminal
        $ HTTPBIN_POD=$(oc get pod -l app=httpbin -n "${VERIFY_NS}" \
          --kubeconfig="${CLUSTER_A_KUBECONFIG}" -o jsonpath="{.items[0].metadata.name}")
        ```

    2.  Export the Envoy sidecar certificate chain for the `httpbin` pod on Cluster A:

        ``` terminal
        $ istioctl --kubeconfig="${CLUSTER_A_KUBECONFIG}" proxy-config secret "${HTTPBIN_POD}" \
          -n "${VERIFY_NS}" -o json \
          | jq -r '.dynamicActiveSecrets[0].secret.tlsCertificate.certificateChain.inlineBytes' \
          | base64 --decode > chain-a.pem
        ```

    3.  Confirm the certificate was issued by SPIRE on Cluster A:

        ``` terminal
        $ openssl x509 -in chain-a.pem -text | grep SPIRE
        ```

8.  Verify the Envoy sidecar certificate on Cluster B by running the following commands:

    1.  Get the `httpbin` pod name on Cluster B:

        ``` terminal
        $ HTTPBIN_POD=$(oc get pod -l app=httpbin -n "${VERIFY_NS}" \
          --kubeconfig="${CLUSTER_B_KUBECONFIG}" -o jsonpath="{.items[0].metadata.name}")
        ```

    2.  Export the Envoy sidecar certificate chain for the `httpbin` pod on Cluster B:

        ``` terminal
        $ istioctl --kubeconfig="${CLUSTER_B_KUBECONFIG}" proxy-config secret "${HTTPBIN_POD}" \
          -n "${VERIFY_NS}" -o json \
          | jq -r '.dynamicActiveSecrets[0].secret.tlsCertificate.certificateChain.inlineBytes' \
          | base64 --decode > chain-b.pem
        ```

    3.  Confirm the certificate was issued by SPIRE on Cluster B:

        ``` terminal
        $ openssl x509 -in chain-b.pem -text | grep SPIRE
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` text
         Issuer: C=US, O=RH, CN=<APP_DOMAIN>/serialNumber=...
                Subject: C=US, O=SPIRE
        ```

        </div>

        If you see `SPIRE` in both `Issuer` and `Subject` on each cluster, Red Hat OpenShift Service Mesh is obtaining workload certificates from SPIRE rather than the Istio built-in CA.

9.  Remove the verification namespace from both clusters by running the following commands:

    1.  Remove the verification namespace from Cluster A:

        ``` terminal
        $ oc delete namespace ${VERIFY_NS} --kubeconfig="${CLUSTER_A_KUBECONFIG}" --ignore-not-found
        ```

    2.  Remove the verification namespace from Cluster B:

        ``` terminal
        $ oc delete namespace ${VERIFY_NS} --kubeconfig="${CLUSTER_B_KUBECONFIG}" --ignore-not-found
        ```

</div>

# Verifying workload mTLS with SPIRE-issued identities on each cluster

Deploy `httpbin` and `curl` test workloads with SPIFFE Runtime Environment (SPIRE) sidecar injection on both clusters, enable `STRICT` mTLS with `ISTIO_MUTUAL`, and verify HTTP connectivity on each cluster. This confirms workloads use SPIRE-issued certificates under `STRICT` mTLS.

<div>

<div class="title">

Prerequisites

</div>

- You have verified that SPIRE is integrated with Istio on each cluster. For more information, see "Verifying SPIRE integration with Istio on each cluster".

- The environment variables from the "Preparing the environment for multi-cluster SPIFFE Runtime Environment federation" and "Deploying SPIFFE Runtime Environment with federation on both clusters" procedures are set.

- Istiod is running and ready on both clusters.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set the test environment variables by running the following commands:

    1.  Set the test namespace environment variable:

        ``` terminal
        $ export TPJ=test-ossm-with-ztwim
        ```

    2.  Set the SPIFFE audience environment variable:

        ``` terminal
        $ export SPIFFE_AUDIENCE="sky-computing-demo"
        ```

2.  Prepare the test namespace on both clusters by running the following commands:

    1.  Create the test namespace on Cluster A:

        ``` terminal
        $ oc create namespace ${TPJ} --kubeconfig="${CLUSTER_A_KUBECONFIG}" 2>/dev/null || true
        ```

    2.  Enable Istio injection for the test namespace on Cluster A:

        ``` terminal
        $ oc label namespace ${TPJ} istio-injection=enabled \
          --kubeconfig="${CLUSTER_A_KUBECONFIG}" --overwrite
        ```

    3.  Create the test namespace on Cluster B:

        ``` terminal
        $ oc create namespace ${TPJ} --kubeconfig="${CLUSTER_B_KUBECONFIG}" 2>/dev/null || true
        ```

    4.  Enable Istio injection for the test namespace on Cluster B:

        ``` terminal
        $ oc label namespace ${TPJ} istio-injection=enabled \
          --kubeconfig="${CLUSTER_B_KUBECONFIG}" --overwrite
        ```

3.  Create the `httpbin` server on Cluster A by running the following command:

    1.  Create a YAML file that defines the `httpbin` `ServiceAccount`, `Service`, and `Deployment` on Cluster A:

        ``` yaml
        apiVersion: v1
        kind: ServiceAccount
        metadata:
          name: httpbin
          namespace: ${TPJ}
        ---
        apiVersion: v1
        kind: Service
        metadata:
          name: httpbin
          namespace: ${TPJ}
          labels:
            app: httpbin
            service: httpbin
        spec:
          ports:
          - name: http-ex-spiffe
            port: 443
            targetPort: 8080
          - name: http
            port: 80
            targetPort: 8080
          selector:
            app: httpbin
        ---
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: httpbin
          namespace: ${TPJ}
        spec:
          replicas: 1
          selector:
            matchLabels:
              app: httpbin
              version: v1
          template:
            metadata:
              annotations:
                inject.istio.io/templates: "sidecar,spire"
                spiffe.io/audience: "${SPIFFE_AUDIENCE}"
              labels:
                app: httpbin
                version: v1
            spec:
              serviceAccountName: httpbin
              containers:
              - image: docker.io/mccutchen/go-httpbin:v2.15.0
                imagePullPolicy: IfNotPresent
                name: httpbin
                ports:
                - containerPort: 8080
        ```

    2.  Apply the YAML file on Cluster A by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_A_KUBECONFIG}" -f <filename>
        ```

4.  Create the `httpbin` server on Cluster B by running the following command:

    1.  Create a YAML file that defines the `httpbin` `ServiceAccount`, `Service`, and `Deployment` on Cluster B:

        ``` yaml
        apiVersion: v1
        kind: ServiceAccount
        metadata:
          name: httpbin
          namespace: ${TPJ}
        ---
        apiVersion: v1
        kind: Service
        metadata:
          name: httpbin
          namespace: ${TPJ}
          labels:
            app: httpbin
            service: httpbin
        spec:
          ports:
          - name: http-ex-spiffe
            port: 443
            targetPort: 8080
          - name: http
            port: 80
            targetPort: 8080
          selector:
            app: httpbin
        ---
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: httpbin
          namespace: ${TPJ}
        spec:
          replicas: 1
          selector:
            matchLabels:
              app: httpbin
              version: v1
          template:
            metadata:
              annotations:
                inject.istio.io/templates: "sidecar,spire"
                spiffe.io/audience: "${SPIFFE_AUDIENCE}"
              labels:
                app: httpbin
                version: v1
            spec:
              serviceAccountName: httpbin
              containers:
              - image: docker.io/mccutchen/go-httpbin:v2.15.0
                imagePullPolicy: IfNotPresent
                name: httpbin
                ports:
                - containerPort: 8080
        ```

    2.  Apply the YAML file on Cluster B by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_B_KUBECONFIG}" -f <filename>
        ```

5.  Wait for the `httpbin` deployment to become available on both clusters by running the following commands:

    1.  Wait for the `httpbin` deployment on Cluster A:

        ``` terminal
        $ oc rollout status deployment/httpbin \
          -n "${TPJ}" --kubeconfig="${CLUSTER_A_KUBECONFIG}" --timeout=300s
        ```

    2.  Wait for the `httpbin` deployment on Cluster B:

        ``` terminal
        $ oc rollout status deployment/httpbin \
          -n "${TPJ}" --kubeconfig="${CLUSTER_B_KUBECONFIG}" --timeout=300s
        ```

6.  Create the `curl` client on Cluster A by running the following command:

    1.  Create a YAML file that defines the `curl` `ServiceAccount`, `Service`, and `Deployment` on Cluster A:

        ``` yaml
        apiVersion: v1
        kind: ServiceAccount
        metadata:
          name: curl
          namespace: ${TPJ}
        ---
        apiVersion: v1
        kind: Service
        metadata:
          name: curl
          namespace: ${TPJ}
          labels:
            app: curl
            service: curl
        spec:
          ports:
          - port: 80
            name: http
          selector:
            app: curl
        ---
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: curl
          namespace: ${TPJ}
        spec:
          replicas: 1
          selector:
            matchLabels:
              app: curl
          template:
            metadata:
              annotations:
                inject.istio.io/templates: "sidecar,spire"
                spiffe.io/audience: "${SPIFFE_AUDIENCE}"
              labels:
                app: curl
            spec:
              terminationGracePeriodSeconds: 0
              serviceAccountName: curl
              containers:
              - name: curl
                image: curlimages/curl:8.16.0
                command:
                - /bin/sh
                - -c
                - sleep inf
                imagePullPolicy: IfNotPresent
        ```

    2.  Apply the YAML file on Cluster A by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_A_KUBECONFIG}" -f <filename>
        ```

7.  Create the `curl` client on Cluster B by running the following command:

    1.  Create a YAML file that defines the `curl` `ServiceAccount`, `Service`, and `Deployment` on Cluster B:

        ``` yaml
        apiVersion: v1
        kind: ServiceAccount
        metadata:
          name: curl
          namespace: ${TPJ}
        ---
        apiVersion: v1
        kind: Service
        metadata:
          name: curl
          namespace: ${TPJ}
          labels:
            app: curl
            service: curl
        spec:
          ports:
          - port: 80
            name: http
          selector:
            app: curl
        ---
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: curl
          namespace: ${TPJ}
        spec:
          replicas: 1
          selector:
            matchLabels:
              app: curl
          template:
            metadata:
              annotations:
                inject.istio.io/templates: "sidecar,spire"
                spiffe.io/audience: "${SPIFFE_AUDIENCE}"
              labels:
                app: curl
            spec:
              terminationGracePeriodSeconds: 0
              serviceAccountName: curl
              containers:
              - name: curl
                image: curlimages/curl:8.16.0
                command:
                - /bin/sh
                - -c
                - sleep inf
                imagePullPolicy: IfNotPresent
        ```

    2.  Apply the YAML file on Cluster B by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_B_KUBECONFIG}" -f <filename>
        ```

8.  Wait for the `curl` deployment to become available on both clusters by running the following commands:

    1.  Wait for the `curl` deployment on Cluster A:

        ``` terminal
        $ oc rollout status deployment/curl \
          -n "${TPJ}" --kubeconfig="${CLUSTER_A_KUBECONFIG}" --timeout=300s
        ```

    2.  Wait for the `curl` deployment on Cluster B:

        ``` terminal
        $ oc rollout status deployment/curl \
          -n "${TPJ}" --kubeconfig="${CLUSTER_B_KUBECONFIG}" --timeout=300s
        ```

9.  Verify that the `curl` client can reach `httpbin` on both clusters before enabling `STRICT` mTLS by running the following commands:

    1.  Verify connectivity on Cluster A:

        ``` terminal
        $ oc exec deploy/curl -n "${TPJ}" --kubeconfig="${CLUSTER_A_KUBECONFIG}" -it -- \
          curl -s -o /dev/null -w "%{http_code}" http://httpbin
        ```

    2.  Verify connectivity on Cluster B:

        ``` terminal
        $ oc exec deploy/curl -n "${TPJ}" --kubeconfig="${CLUSTER_B_KUBECONFIG}" -it -- \
          curl -s -o /dev/null -w "%{http_code}" http://httpbin
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        200
        ```

        </div>

        You must receive an HTTP `200` status code on each cluster.

10. Enable `STRICT` mTLS between the services on Cluster A by running the following command:

    1.  Create a YAML file that defines the `PeerAuthentication` and `DestinationRule` resources on Cluster A:

        ``` yaml
        apiVersion: security.istio.io/v1beta1
        kind: PeerAuthentication
        metadata:
          name: default
          namespace: ${TPJ}
        spec:
          mtls:
            mode: STRICT
        ---
        apiVersion: networking.istio.io/v1
        kind: DestinationRule
        metadata:
          name: curl
          namespace: ${TPJ}
        spec:
          host: curl
          trafficPolicy:
            tls:
              mode: ISTIO_MUTUAL
        ---
        apiVersion: networking.istio.io/v1
        kind: DestinationRule
        metadata:
          name: httpbin
          namespace: ${TPJ}
        spec:
          host: httpbin
          trafficPolicy:
            tls:
              mode: ISTIO_MUTUAL
        ```

    2.  Apply the YAML file on Cluster A by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_A_KUBECONFIG}" -f <filename>
        ```

11. Enable `STRICT` mTLS between the services on Cluster B by running the following command:

    1.  Create a YAML file that defines the `PeerAuthentication` and `DestinationRule` resources on Cluster B:

        ``` yaml
        apiVersion: security.istio.io/v1beta1
        kind: PeerAuthentication
        metadata:
          name: default
          namespace: ${TPJ}
        spec:
          mtls:
            mode: STRICT
        ---
        apiVersion: networking.istio.io/v1
        kind: DestinationRule
        metadata:
          name: curl
          namespace: ${TPJ}
        spec:
          host: curl
          trafficPolicy:
            tls:
              mode: ISTIO_MUTUAL
        ---
        apiVersion: networking.istio.io/v1
        kind: DestinationRule
        metadata:
          name: httpbin
          namespace: ${TPJ}
        spec:
          host: httpbin
          trafficPolicy:
            tls:
              mode: ISTIO_MUTUAL
        ```

    2.  Apply the YAML file on Cluster B by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_B_KUBECONFIG}" -f <filename>
        ```

12. Verify that the `curl` client can reach `httpbin` on both clusters with `STRICT` mTLS enabled by running the following commands:

    1.  Verify connectivity on Cluster A:

        ``` terminal
        $ oc exec deploy/curl -n "${TPJ}" --kubeconfig="${CLUSTER_A_KUBECONFIG}" -it -- \
          curl -s -o /dev/null -w "%{http_code}" http://httpbin
        ```

    2.  Verify connectivity on Cluster B:

        ``` terminal
        $ oc exec deploy/curl -n "${TPJ}" --kubeconfig="${CLUSTER_B_KUBECONFIG}" -it -- \
          curl -s -o /dev/null -w "%{http_code}" http://httpbin
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        200
        ```

        </div>

        If you receive an HTTP `200` status code on each cluster, Red Hat OpenShift Service Mesh workloads are communicating under `STRICT` mTLS using SPIRE-issued identities.

13. Remove the test namespace from both clusters by running the following commands:

    1.  Remove the test namespace from Cluster A:

        ``` terminal
        $ oc delete namespace ${TPJ} --kubeconfig="${CLUSTER_A_KUBECONFIG}" --ignore-not-found
        ```

    2.  Remove the test namespace from Cluster B:

        ``` terminal
        $ oc delete namespace ${TPJ} --kubeconfig="${CLUSTER_B_KUBECONFIG}" --ignore-not-found
        ```

</div>

# Deploying east-west gateways

Deploy SPIRE-enabled east-west gateways on both clusters using Helm. Red Hat OpenShift Service Mesh uses east-west gateways to connect cluster networks and enable secure cross-cluster communication in a multi-cluster mesh.

<div>

<div class="title">

Prerequisites

</div>

- You deployed the Istio custom resource with the federation configuration. For more information, see "Deploying the Istio custom resource with the federation configuration".

- The environment variables from the "Preparing the environment for multi-cluster SPIFFE Runtime Environment federation" and "Deploying SPIFFE Runtime Environment with federation on both clusters" procedures are set.

- Federated `ClusterSPIFFEID` resources exist on both clusters.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Add the Istio Helm repository by running the following command:

    ``` terminal
    $ helm repo add istio https://istio-release.storage.googleapis.com/charts
    ```

2.  Update the Istio Helm repository by running the following command:

    ``` terminal
    $ helm repo update
    ```

3.  Grant security context constraints (SCC) permissions on Cluster A by running the following command:

    ``` terminal
    $ oc adm policy add-scc-to-user anyuid \
      -z istio-eastwestgateway -n istio-system --kubeconfig="${CLUSTER_A_KUBECONFIG}"
    ```

4.  Grant security context constraints (SCC) permissions on Cluster B by running the following command:

    ``` terminal
    $ oc adm policy add-scc-to-user anyuid \
      -z istio-eastwestgateway -n istio-system --kubeconfig="${CLUSTER_B_KUBECONFIG}"
    ```

5.  Install the Istio gateway on Cluster A by running the following command:

    ``` terminal
    $ helm upgrade --install istio-eastwestgateway istio/gateway \
      -n istio-system \
      --set-json 'podAnnotations={"inject.istio.io/templates":"gateway,spireGw"}' \
      --set name=istio-eastwestgateway \
      --set networkGateway="${NETWORK_A}" \
      --kubeconfig="${CLUSTER_A_KUBECONFIG}"
    ```

6.  Install the Istio gateway on Cluster B by running the following command:

    ``` terminal
    $ helm upgrade --install istio-eastwestgateway istio/gateway \
      -n istio-system \
      --set-json 'podAnnotations={"inject.istio.io/templates":"gateway,spireGw"}' \
      --set name=istio-eastwestgateway \
      --set networkGateway="${NETWORK_B}" \
      --kubeconfig="${CLUSTER_B_KUBECONFIG}"
    ```

7.  Wait for the east-west gateway to become available on Cluster A by running the following command:

    ``` terminal
    $ oc wait --for=condition=Available deployment/istio-eastwestgateway \
      --kubeconfig="${CLUSTER_A_KUBECONFIG}" -n istio-system --timeout=300s
    ```

8.  Wait for the east-west gateway to become available on Cluster B by running the following command:

    ``` terminal
    $ oc wait --for=condition=Available deployment/istio-eastwestgateway \
      --kubeconfig="${CLUSTER_B_KUBECONFIG}" -n istio-system --timeout=300s
    ```

9.  Create the cross-network `Gateway` custom resource (CR) on Cluster A by running the following command:

    1.  Create a YAML file that defines the `Gateway` CR on Cluster A:

        ``` yaml
        apiVersion: networking.istio.io/v1alpha3
        kind: Gateway
        metadata:
          name: cross-network-gateway
          namespace: istio-system
        spec:
          selector:
            istio: eastwestgateway
          servers:
            - port:
                number: 15443
                name: tls
                protocol: TLS
              tls:
                mode: AUTO_PASSTHROUGH
              hosts:
                - "*.local"
        ```

    2.  Apply the YAML file on Cluster A by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_A_KUBECONFIG}" -f <filename>
        ```

10. Create the cross-network `Gateway` CR on Cluster B by running the following command:

    1.  Create a YAML file that defines the `Gateway` CR on Cluster B:

        ``` yaml
        apiVersion: networking.istio.io/v1alpha3
        kind: Gateway
        metadata:
          name: cross-network-gateway
          namespace: istio-system
        spec:
          selector:
            istio: eastwestgateway
          servers:
            - port:
                number: 15443
                name: tls
                protocol: TLS
              tls:
                mode: AUTO_PASSTHROUGH
              hosts:
                - "*.local"
        ```

    2.  Apply the YAML file on Cluster B by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_B_KUBECONFIG}" -f <filename>
        ```

        The `Gateway` CRs configure the east-west gateway deployment to accept cross-cluster TLS traffic on port 15443 using `AUTO_PASSTHROUGH` mode. This preserves SPIRE-issued certificates for end-to-end mTLS.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the cross-network `Gateway` exists on Cluster A by running the following command:

    ``` terminal
    $ oc get gateway cross-network-gateway -n istio-system \
      --kubeconfig="${CLUSTER_A_KUBECONFIG}" \
      -o jsonpath='{.spec.servers[0].tls.mode}{"\n"}'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` text
    AUTO_PASSTHROUGH
    ```

    </div>

2.  Verify that the cross-network `Gateway` exists on Cluster B by running the following command:

    ``` terminal
    $ oc get gateway cross-network-gateway -n istio-system \
      --kubeconfig="${CLUSTER_B_KUBECONFIG}" \
      -o jsonpath='{.spec.servers[0].tls.mode}{"\n"}'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` text
    AUTO_PASSTHROUGH
    ```

    </div>

</div>

# Exchanging remote secrets

Create remote secrets on both clusters so `Istiod` can discover services in the peer cluster and route cross-cluster traffic through the east-west gateways.

<div>

<div class="title">

Prerequisites

</div>

- You have deployed the east-west gateway, including the cross-network `Gateway` CR on both clusters. For more information, see "Deploying east-west gateways".

- The environment variables from the "Preparing the environment for multi-cluster SPIFFE Runtime Environment federation" and "Deploying SPIFFE Runtime Environment with federation on both clusters" procedures are set.

- The `istioctl` CLI is available and configured for both clusters.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an Istio remote secret on Cluster A by running the following command:

    ``` terminal
    $ istioctl create-remote-secret \
      --kubeconfig="${CLUSTER_A_KUBECONFIG}" \
      --name="${CLUSTER_A}" \
      --istioNamespace=istio-system | \
      oc apply --kubeconfig="${CLUSTER_B_KUBECONFIG}" -f -
    ```

2.  Create an Istio remote secret on Cluster B by running the following command:

    ``` terminal
    $ istioctl create-remote-secret \
      --kubeconfig="${CLUSTER_B_KUBECONFIG}" \
      --name="${CLUSTER_B}" \
      --istioNamespace=istio-system | \
      oc apply --kubeconfig="${CLUSTER_A_KUBECONFIG}" -f -
    ```

3.  Verify that the remote cluster is synced on Cluster A by running the following command:

    ``` terminal
    $ istioctl remote-clusters --kubeconfig="${CLUSTER_A_KUBECONFIG}"
    ```

    The output must show `${CLUSTER_B}` with status `synced`.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` text
    NAME         STATUS   SECRET
    cluster-b    synced   istio-remote-secret-cluster-b
    ```

    </div>

4.  Verify that the remote cluster is synced on Cluster B by running the following command:

    ``` terminal
    $ istioctl remote-clusters --kubeconfig="${CLUSTER_B_KUBECONFIG}"
    ```

    The output must show `${CLUSTER_A}` with status `synced`.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` text
    NAME         STATUS   SECRET
    cluster-a    synced   istio-remote-secret-cluster-a
    ```

    </div>

</div>

# Verifying cross-cluster service communication

Verify cross-cluster service communication between Red Hat OpenShift Service Mesh clusters using sample workloads. This confirms SPIRE-issued identities and federated mesh routing enable end-to-end cross-cluster communication.

<div>

<div class="title">

Prerequisites

</div>

- You have deployed east-west gateways and created the cross-network `Gateway` CR on both clusters.

- You have exchanged remote secrets between clusters.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set the sample namespace environment variable by running the following command:

    ``` terminal
    $ export SAMPLE_NS=sample
    ```

2.  Create the `sample` namespace on Cluster A by running the following command:

    ``` terminal
    $ oc create namespace ${SAMPLE_NS} --kubeconfig="${CLUSTER_A_KUBECONFIG}" 2>/dev/null || true
    ```

3.  Enable Istio injection for the `sample` namespace on Cluster A by running the following command:

    ``` terminal
    $ oc label namespace ${SAMPLE_NS} istio-injection=enabled \
      --kubeconfig="${CLUSTER_A_KUBECONFIG}" --overwrite
    ```

4.  Create the `sample` namespace on Cluster B by running the following command:

    ``` terminal
    $ oc create namespace ${SAMPLE_NS} --kubeconfig="${CLUSTER_B_KUBECONFIG}" 2>/dev/null || true
    ```

5.  Enable Istio injection for the `sample` namespace on Cluster B by running the following command:

    ``` terminal
    $ oc label namespace ${SAMPLE_NS} istio-injection=enabled \
      --kubeconfig="${CLUSTER_B_KUBECONFIG}" --overwrite
    ```

6.  Install the Istio `HelloWorld` `Service` in Cluster B by running the following command:

    1.  Create a YAML file that defines the `HelloWorld` `Service` in Cluster B:

        ``` yaml
        apiVersion: v1
        kind: Service
        metadata:
          name: helloworld
          labels:
            app: helloworld
            service: helloworld
        spec:
          ports:
          - port: 5000
            name: http
          selector:
            app: helloworld
        ```

    2.  Apply the YAML file in Cluster B by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_B_KUBECONFIG}" -n ${SAMPLE_NS} -f <filename>
        ```

7.  Install the `helloworld-v1` `Deployment` in Cluster B by running the following command:

    1.  Create a YAML file that defines the `helloworld-v1` `Deployment` in Cluster B:

        ``` yaml
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: helloworld-v1
          labels:
            app: helloworld
            version: v1
        spec:
          replicas: 1
          selector:
            matchLabels:
              app: helloworld
              version: v1
          template:
            metadata:
              labels:
                app: helloworld
                version: v1
            spec:
              containers:
              - name: helloworld
                image: registry.istio.io/release/examples-helloworld-v1:1.0
                resources:
                  requests:
                    cpu: "100m"
                imagePullPolicy: IfNotPresent
                ports:
                - containerPort: 5000
        ```

    2.  Apply the YAML file in Cluster B by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_B_KUBECONFIG}" -n ${SAMPLE_NS} -f <filename>
        ```

8.  Install the Istio `HelloWorld` `Service` in Cluster A by running the following command:

    1.  Create a YAML file that defines the `HelloWorld` `Service` in Cluster A:

        ``` yaml
        apiVersion: v1
        kind: Service
        metadata:
          name: helloworld
          labels:
            app: helloworld
            service: helloworld
        spec:
          ports:
          - port: 5000
            name: http
          selector:
            app: helloworld
        ```

    2.  Apply the YAML file in Cluster A by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_A_KUBECONFIG}" -n ${SAMPLE_NS} -f <filename>
        ```

9.  Install the `sleep` client in Cluster A by running the following command:

    1.  Create a YAML file that defines the `sleep` `ServiceAccount`, `Service`, and `Deployment` in Cluster A:

        ``` yaml
        apiVersion: v1
        kind: ServiceAccount
        metadata:
          name: sleep
        ---
        apiVersion: v1
        kind: Service
        metadata:
          name: sleep
          labels:
            app: sleep
            service: sleep
        spec:
          ports:
          - port: 80
            name: http
          selector:
            app: sleep
        ---
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: sleep
        spec:
          replicas: 1
          selector:
            matchLabels:
              app: sleep
          template:
            metadata:
              labels:
                app: sleep
            spec:
              terminationGracePeriodSeconds: 0
              serviceAccountName: sleep
              containers:
              - name: sleep
                image: docker.io/curlimages/curl:8.16.0
                command: ["/bin/sleep", "infinity"]
                imagePullPolicy: IfNotPresent
                volumeMounts:
                - mountPath: /etc/sleep/tls
                  name: secret-volume
              volumes:
              - name: secret-volume
                secret:
                  secretName: sleep-secret
                  optional: true
        ```

    2.  Apply the YAML file in Cluster A by running the following command:

        ``` terminal
        $ oc apply --kubeconfig="${CLUSTER_A_KUBECONFIG}" -n ${SAMPLE_NS} -f <filename>
        ```

10. Add the SPIRE injection template to the `sleep` application in Cluster A by running the following command:

    ``` terminal
    $ oc patch deploy sleep \
        -n ${SAMPLE_NS} \
        --type='merge' \
        --kubeconfig="${CLUSTER_A_KUBECONFIG}" \
        -p '{"spec": {"template": {"metadata": {"annotations": {"inject.istio.io/templates": "sidecar,spire"}}}}}'
    ```

11. Add the SPIRE injection template to the `HelloWorld` application in Cluster B by running the following command:

    ``` terminal
    $ oc patch deploy helloworld-v1 \
       -n ${SAMPLE_NS} \
       --type='merge' \
       --kubeconfig="${CLUSTER_B_KUBECONFIG}" \
        -p '{"spec": {"template": {"metadata": {"annotations": {"inject.istio.io/templates": "sidecar,spire"}}}}}'
    ```

12. Wait for the `sleep` deployment to become available on Cluster A by running the following command:

    ``` terminal
    $ oc rollout status deploy/sleep --kubeconfig "${CLUSTER_A_KUBECONFIG}" -n ${SAMPLE_NS} --timeout=300s
    ```

13. Wait for the `helloworld-v1` deployment to become available on Cluster B by running the following command:

    ``` terminal
    $ oc rollout status deploy/helloworld-v1 --kubeconfig "${CLUSTER_B_KUBECONFIG}" -n ${SAMPLE_NS} --timeout=300s
    ```

14. Verify that the `sleep` pod uses a SPIRE-issued identity by running the following command:

    ``` terminal
    $ oc exec deploy/sleep -n ${SAMPLE_NS} --kubeconfig="${CLUSTER_A_KUBECONFIG}" -c istio-proxy -- \
      curl -s localhost:15000/certs | jq -r '.certificates[0].cert_chain[0].subject_alt_names[0].uri'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` text
    spiffe://${CLUSTER_A_TRUST_DOMAIN}/ns/sample/sa/sleep
    ```

    </div>

15. Verify that the `sleep` pod on Cluster A can reach the `helloworld.sample` service by running the following command:

    ``` terminal
    $ oc exec deploy/sleep \
      -n ${SAMPLE_NS} \
      --kubeconfig="${CLUSTER_A_KUBECONFIG}" \
      -- curl -sS helloworld.sample:5000/hello
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` text
    Hello version: v1, instance: helloworld-v1-5859666d7-pcb8v
    ```

    </div>

</div>

# Additional resources

- [Multi-cluster configuration overview](https://docs.redhat.com/en/documentation/red_hat_openshift_service_mesh/latest/html-single/installing/index#ossm-multi-cluster-configuration-overview_ossm-multi-cluster-topologies)
