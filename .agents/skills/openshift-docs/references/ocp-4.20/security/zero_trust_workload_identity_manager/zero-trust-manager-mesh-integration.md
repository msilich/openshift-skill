<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Deploy and configure SPIFFE Runtime Environment as the certificate authority (CA) for Red Hat OpenShift Service Mesh workloads, replacing the Istio built-in CA with SPIFFE-compliant identities and automatically rotated short-lived certificates.

# SPIRE integration with Red Hat OpenShift Service Mesh

Red Hat OpenShift Service Mesh integrates with Zero Trust Workload Identity Manager so Envoy sidecars obtain mTLS certificates from Secure Production Identity Framework for Everyone (SPIFFE) instead of Istio’s built-in CA, enabling cryptographically verified workload identities.

SPIRE provides cryptographic workload identities based on the Secure Production Identity Framework for Everyone (SPIFFE) standard. This integration enables a zero-trust security model where workload identities are cryptographically verified rather than relying on network-based authentication.

## Component overview

The following table summarizes the main components in a single-cluster SPIFFE and Red Hat OpenShift Service Mesh integration and what each one does.

| Component | Purpose |
|----|----|
| **Zero Trust Workload Identity Manager** | Manages SPIRE deployment on OpenShift Container Platform |
| **SPIRE Server** | Certificate Authority; issues SVIDs |
| **SPIRE Agent** | Runs on each node; provides SDS API to workloads |
| **SPIFFE CSI Driver** | Mounts SPIRE socket into pods |
| **ClusterSPIFFEID** | Registers which pods get which identities |
| **Red Hat OpenShift Service Mesh Operator** | Manages Istio deployment |
| **Istiod** | Istio control plane |
| **Envoy Sidecar** | Proxy in each pod; uses SPIRE for certificates |

# SPIRE integration architecture components

Learn about the key components in the SPIRE integration architecture and how they work together to enable zero-trust workload identity and automated certificate management for secure mTLS connections in Red Hat OpenShift Service Mesh.

Zero Trust Workload Identity Manager
Manages the SPIRE deployment lifecycle on OpenShift Container Platform, including custom resources for SPIRE Server, SPIRE Agent, and related components.

SPIRE Server
Acts as the certificate authority that issues SPIFFE Verifiable Identity Documents (SVIDs) to authenticated workloads.

SPIRE Agent
Runs as a DaemonSet on each cluster node, providing the Envoy Secret Discovery Service (SDS) API to workloads on that node.

SPIFFE CSI Driver
Mounts the SPIRE Agent UNIX domain socket into pods, enabling secure communication between Envoy sidecars and the SPIRE Agent.

Red Hat OpenShift Service Mesh
Manages the Istio deployment through the `servicemeshoperator3` Operator.

Istiod
The Istio control plane that configures Envoy proxies but delegates certificate issuance to SPIRE.

Envoy sidecar
The proxy injected into each workload pod that uses SPIRE-issued certificates for mTLS connections.

# Deploying SPIRE operands for Red Hat OpenShift Service Mesh integration

Deploy SPIRE operands by creating the `ZeroTrustWorkloadIdentityManager` custom resource (CR) and related SPIRE operand CRs together. A running SPIRE deployment is required before you configure Red Hat OpenShift Service Mesh to use SPIRE-issued certificates for workload mTLS.

<div>

<div class="title">

Prerequisites

</div>

- You have installed Zero Trust Workload Identity Manager.

- The OpenShift CLI (`oc`) is configured with access to the cluster.

- You have permissions to create custom resources in the `zero-trust-workload-identity-manager` namespace.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set the environment variables by running the following commands:

    ``` terminal
    $ export TRUST_DOMAIN=ocp.one
    $ export ZTWIM_NS=zero-trust-workload-identity-manager
    $ export JWT_ISSUER="https://oidc-discovery.$(oc get ingresses.config/cluster -o jsonpath={.spec.domain})"
    ```

2.  Deploy all SPIRE operand CRs, including the `ZeroTrustWorkloadIdentityManager` CR:

    1.  Create the `ZeroTrustWorkloadIdentityManager` CR:

        ``` yaml
        $ oc apply -f - <<EOF
        apiVersion: operator.openshift.io/v1alpha1
        kind: ZeroTrustWorkloadIdentityManager
        metadata:
         name: cluster
         labels:
           app.kubernetes.io/name: zero-trust-workload-identity-manager
           app.kubernetes.io/managed-by: zero-trust-workload-identity-manager
        spec:
          trustDomain: ${TRUST_DOMAIN}
          clusterName: ""
          bundleConfigMap: "spire-bundle"
        EOF
        ```

    2.  Create the `SpireServer` CR:

        ``` yaml
        $ cat <<EOF | oc apply -f -
        apiVersion: operator.openshift.io/v1alpha1
        kind: SpireServer
        metadata:
         name: cluster
        spec:
          logLevel: "info"
          logFormat: "text"
          jwtIssuer: $JWT_ISSUER
          caValidity: "24h"
          defaultX509Validity: "1h"
          defaultJWTValidity: "5m"
          caKeytype: “rsa-2048”
          jwtKeyType: "rsa-2048"
          keyManager: “”
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
        EOF
        ```

    3.  Wait for the SPIRE Server to become ready by running the following commands:

        ``` terminal
        $ until oc get statefulset/spire-server -n "${ZTWIM_NS}" &> /dev/null; do sleep 3; done
        ```

        ``` terminal
        $ kubectl rollout status statefulset/spire-server -n "${ZTWIM_NS}" --timeout=300s
        ```

    4.  Create the `SpireAgent` CR:

        ``` yaml
        $ cat <<EOF | oc apply -f -
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
            disableContainerSelectors: "false"
            useNewContainerLocator: "true"
        EOF
        ```

    5.  Wait for the SPIRE Agent to become ready by running the following commands:

        ``` terminal
        $ until oc get daemonset/spire-agent -n "${ZTWIM_NS}" &> /dev/null; do sleep 3; done
        ```

        ``` terminal
        $ kubectl rollout status daemonset/spire-agent -n "${ZTWIM_NS}" --timeout=300s
        ```

    6.  Deploy the `SpiffeCSIDriver` CR:

        ``` yaml
        $ cat <<EOF | oc apply -f -
        apiVersion: operator.openshift.io/v1alpha1
        kind: SpiffeCSIDriver
        metadata:
          name: cluster
        spec:
          agentSocketPath: '/run/spire/agent-sockets'
          pluginName: "csi.spiffe.io"
        EOF
        ```

    7.  Wait for the SPIFFE CSI Driver to become ready by running the following commands:

        ``` terminal
        $ until oc get daemonset/spire-spiffe-csi-driver -n "${ZTWIM_NS}" &> /dev/null; do sleep 3; done
        ```

        ``` terminal
        $ kubectl rollout status daemonset/spire-spiffe-csi-driver -n "${ZTWIM_NS}" --timeout=300s
        ```

    8.  Deploy the `SpireOIDCDiscoveryProvider` CR:

        ``` terminal
        $ export OIDC_DISCOVERY_CONFIG_MAP=spire-spiffe-oidc-discovery-provider
        ```

        ``` yaml
        $ cat <<EOF | oc apply -f -
        apiVersion: operator.openshift.io/v1alpha1
        kind: SpireOIDCDiscoveryProvider
        metadata:
          name: cluster
        spec:
          logLevel: "info"
          logFormat: "text"
          csiDriverName: "csi.spiffe.io"
          jwtIssuer: $JWT_ISSUER
          replicaCount: 1
          managedRoute: "true"
        EOF
        ```

    9.  Wait for the OIDC Discovery Provider to be created by running the following commands:

        ``` terminal
        $ until oc get deployment spire-spiffe-oidc-discovery-provider -n "${ZTWIM_NS}" &> /dev/null; do sleep 3; done
        ```

        ``` terminal
        $ oc wait --for=condition=Available deployment/spire-spiffe-oidc-discovery-provider -n "${ZTWIM_NS}" --timeout=300s
        ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that Zero Trust Workload Identity Manager is installed:

    1.  Deploy the client workload and try to fetch a workload SVID:

        ``` yaml
        $ cat <<EOF | oc apply -f -
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: ztwim-client
          namespace: default
          labels:
            app: ztwim-client
        spec:
          selector:
            matchLabels:
              app: ztwim-client
          template:
            metadata:
              labels:
                app: ztwim-client
            spec:
              containers:
                - name: client
                  image: ghcr.io/spiffe/spire-agent:1.5.1
                  command: ["/opt/spire/bin/spire-agent"]
                  args: [ "api", "watch",  "-socketPath", "/run/spire/sockets/spire-agent.sock" ]
                  volumeMounts:
                    - mountPath: /run/spire/sockets
                      name: spiffe-workload-api
                      readOnly: true
              volumes:
              - name: spiffe-workload-api
                csi:
                  driver: csi.spiffe.io
                  readOnly: true
        EOF
        ```

    2.  Wait for the client deployment to become ready by running the following command:

        ``` terminal
        $ until oc get deployment ztwim-client -n default &> /dev/null; do sleep 3; done
        ```

        ``` terminal
        $ oc wait --for=condition=Available deployment/ztwim-client -n default --timeout=300s
        ```

        ``` terminal
        $ sleep 5
        ```

2.  Verify that the x509 SVID is available by running the following command:

    ``` terminal
    $ oc exec -it \
      "$(oc get \
          pods -o=jsonpath='{.items[0].metadata.name}' \
          -l app=ztwim-client \
          -n default \
       )" -n default -- \
      /opt/spire/bin/spire-agent \
        api fetch -socketPath /run/spire/sockets/spire-agent.sock
    ```

    The expected output is an SVID like the following example:

    ``` text
    Received 1 svid after 29.636075ms

    SPIFFE ID:      spiffe://ocp.one/ns/default/sa/default
    SVID Valid After:    2025-10-21 14:04:03 +0000 UTC
    SVID Valid Until:    2025-10-21 15:04:13 +0000 UTC
    CA #1 Valid After:  2025-10-21 07:38:03 +0000 UTC
    CA #1 Valid Until:  2025-10-22 07:38:13 +0000 UTC
    ```

3.  Verify that the JSON Web Token (JWT) SVID is available by running the following command:

    ``` terminal
    $ oc exec -it \
      "$(oc get \
          pods -o=jsonpath='{.items[0].metadata.name}' \
          -l app=ztwim-client \
          -n default \
       )" -n default -- \
      /opt/spire/bin/spire-agent \
        api fetch jwt -audience=sample-aud -socketPath /run/spire/sockets/spire-agent.sock
    ```

    The expected output is a JWT SVID like the following example:

    ``` text
    token(spiffe://ocp.one/ns/default/sa/default):
        eyJhbGciOiJSUzI1NiIsImtpZCI6Ij....IsIm
    bundle(spiffe://ocp.one):
        {
        "keys": [
            {
                "kty": "RSA",
                "kid": "6k9PfhrAdfajT6jvLvR6bdomFvQxMeGf",
                "n": "wEYTV0ri4OOcdgEVgzN0...KhUEGf0NKxnuaeGQ",
                "e": "AQAB"
            }
        ]
    }
    ```

4.  Remove the client workload by running the following command:

    ``` terminal
    $ oc delete deployment ztwim-client -n default
    ```

</div>

# Deploying Red Hat OpenShift Service Mesh for SPIRE integration

Deploy Red Hat OpenShift Service Mesh by creating the `IstioCNI` and `Istio` CRs with SPIRE integration settings so Envoy sidecars obtain SPIRE-issued certificates for workload mTLS after the SPIRE stack is running.

<div>

<div class="title">

Prerequisites

</div>

- You have installed Zero Trust Workload Identity Manager.

- The OpenShift CLI (`oc`) is configured with access to the cluster.

- You have permissions to create namespaces and custom resources in the `istio-cni` and `istio-system` namespaces.

- You have permissions to read secrets in the `zero-trust-workload-identity-manager` namespace.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set the Istio environment variables by running the following commands:

    ``` terminal
    $ export ZTWIM_NS=zero-trust-workload-identity-manager
    $ export TRUST_DOMAIN=ocp.one
    $ export JWT_ISSUER="https://oidc-discovery.$(oc get ingresses.config/cluster -o jsonpath={.spec.domain})"
    $ export OSSM_NS=istio-system
    $ export OSSM_CNI=istio-cni
    $ export VERIFY_NS=verify-ossm-ztwim
    $ export EXTRA_ROOT_CA="$(oc get secret oidc-serving-cert \
                             -n ${ZTWIM_NS} -o json | \
                             jq -r '.data."tls.crt"' | \
                             base64 -d | \
                             sed 's/^/        /')"
    ```

2.  Create the `IstioCNI` CR to deploy Istio CNI by running the following commands:

    ``` terminal
    $ oc new-project "${OSSM_CNI}" 2>/dev/null || oc project "${OSSM_CNI}"
    ```

    ``` yaml
    $ oc apply -f - <<EOF
    apiVersion: sailoperator.io/v1
    kind: IstioCNI
    metadata:
      name: default
    spec:
      version: <version>
      namespace: ${OSSM_CNI}
    EOF
    ```

    where:

    `spec.version`
    Replace `<version>` with the Istio version supported by your Red Hat OpenShift Service Mesh Operator. You can find supported versions by running `oc get IstioCNI -o jsonpath='{.items[*].spec.version}'` after the Operator is installed.

3.  Wait for Istio CNI to become ready by running the following commands:

    ``` terminal
    $ until oc get daemonset/istio-cni-node -n "${OSSM_CNI}" &> /dev/null; do sleep 3; done
    ```

    ``` terminal
    $ kubectl rollout status daemonset/istio-cni-node -n "${OSSM_CNI}" --timeout=300s
    ```

    The `until` loop waits for the Red Hat OpenShift Service Mesh Operator to create the `istio-cni-node` DaemonSet. The `oc rollout status` command waits for the DaemonSet pods to become ready.

4.  Install the Istio CR with SPIRE integration by running the following commands:

    ``` terminal
    $ oc new-project "${OSSM_NS}" 2>/dev/null
    ```

    ``` yaml
    $ cat <<EOF | oc apply -f -
    apiVersion: sailoperator.io/v1
    kind: Istio
    metadata:
      name: default
    spec:
      namespace: istio-system
      updateStrategy:
        type: InPlace
      values:
        pilot:
          jwksResolverExtraRootCA: |
    ${EXTRA_ROOT_CA}
          env:
            PILOT_JWT_ENABLE_REMOTE_JWKS: "true"
        meshConfig:
          trustDomain: $TRUST_DOMAIN
          defaultConfig:
            proxyMetadata:
              WORKLOAD_IDENTITY_SOCKET_FILE: "spire-agent.sock"
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
            spireGateway: |
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
    EOF
    ```

5.  Wait for all of the resources to become ready by running the following commands:

    ``` terminal
    $ until oc get deployment istiod -n "${OSSM_NS}" &> /dev/null; do sleep 3; done
    ```

    ``` terminal
    $ oc wait --for=condition=Available deployment/istiod -n "${OSSM_NS}" --timeout=300s
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that Istio is integrated with SPIRE:

    1.  Create a test workload with the `spire` injection template by running the following commands:

        ``` terminal
        $ oc new-project "${VERIFY_NS}" 2>/dev/null
        ```

    2.  Enable the sidecar injection by running the following command:

        ``` terminal
        $ oc label namespace "${VERIFY_NS}" istio-injection=enabled
        ```

    3.  Create the `httpbin` workload:

        ``` yaml
        $ cat <<EOF | oc apply -f -
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
        EOF
        ```

    4.  Wait for all of the resources to become ready by running the following commands:

        ``` terminal
        $ until oc get deployment httpbin -n "${VERIFY_NS}" &> /dev/null; do sleep 3; done
        ```

        ``` terminal
        $ oc wait --for=condition=Available deployment/httpbin -n "${VERIFY_NS}" --timeout=300s
        ```

    5.  Verify the SPIRE workload identity by running the following command:

        ``` terminal
        $ HTTPBIN_POD=$(oc get pod -l app=httpbin -n "${VERIFY_NS}" -o jsonpath="{.items[0].metadata.name}")

        $ istioctl proxy-config secret "$HTTPBIN_POD" \
          -n "${VERIFY_NS}" -o json \
          | jq -r '.dynamicActiveSecrets[0].secret.tlsCertificate.certificateChain.inlineBytes' \
          | base64 --decode > chain.pem

        openssl x509 -in chain.pem -text | grep SPIRE
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
         Issuer: C=US, O=RH, CN=<APP_DOMAIN>/serialNumber=...
                Subject: C=US, O=SPIRE
        ```

        </div>

        If you see `SPIRE` in both `Issuer` and `Subject`, the integration is working. Envoy is getting its certificates from SPIRE, not from Istio’s built-in CA.

    6.  Remove the namespace by running the following command:

        ``` terminal
        $ oc delete namespace "${VERIFY_NS}"
        ```

</div>

# Additional resources

- [About OpenShift Service Mesh](https://docs.redhat.com/en/documentation/red_hat_openshift_service_mesh/3.3/html-single/about/index)

- [Installing OpenShift Service Mesh](https://docs.redhat.com/en/documentation/red_hat_openshift_service_mesh/3.3/html-single/installing/index#ossm-supported-platforms-configurations)
