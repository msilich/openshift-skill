<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The Argo CD Agent consists of two components, **Principal** and **Agent** that work together to synchronize applications between the control plane and workload clusters in a hub-and-spoke configuration. Install the Principal component by using Argo CD resources and the Agent component by using Helm charts to complete the Argo CD Agent setup.

For more information, see the Additional Resources section, which includes an architectural overview of the *Argo CD Agent architecture*.

# Prerequisites

- You have installed the Red Hat OpenShift GitOps Operator on two OpenShift Container Platform clusters.

- You have installed the OpenShift CLI (`oc`).

- You have installed a `cluster-scoped Argo CD` instance on the hub cluster.

- You have configured `Apps in any namespace` feature on the hub cluster.

- You have installed `argocd-agentctl` CLI tool.

- You have installed `helm` CLI for your Agent setup. Ensure that the `helm` CLI version is greater than v3.8.0.

- You have reviewed the key Argo CD Agent terms required to understand the Principal and Agent components in the *Argo CD Terminologies* section.

# Argo CD Agent Terminologies

The following definitions help you understand the required namespaces, contexts, and command-line parameters used when configuring Argo CD Agent across hub and spoke clusters.

Principal namespace
Specifies the namespace where you install the Principal component. This namespace is not created by default, you must create it before adding the resources in this namespace. In Argo CD Agent CLI commands, this value is provided using the `--principal-namespace` flag.

Agent namespace
Specifies the namespace hosting the `Agent` component. This namespace is not created by default, you must create it before adding the resources in this namespace. In Argo CD Agent CLI commands, this value is provided using the `--agent-namespace` flag.

Context
A **context** refers to a named configuration in the `oc` CLI that allows you to switch between different clusters. You must be logged in to all clusters and assign distinct context names for the hub and spoke clusters. Examples for cluster names include `principal-cluster`, `hub-cluster`, `managed-agent-cluster`, or `autonomous-agent-cluster`.

Principal context
The context name you provide for the hub (control plane) cluster. For example, if you log in to the hub cluster and rename its context to `principal-cluster`, you specify it in Argo CD Agent CLI commands as `--principal-context principal-cluster`.

Agent context
The context name you provide for the spoke (workload) cluster. For example, if you log in to a spoke cluster and rename its context to `autonomous-agent-cluster`, you specify it in Argo CD Agent CLI commands as `--agent-context autonomous-agent-cluster`.

# Installing the Principal component

You can install the Principal component on the hub cluster by using the Argo CD custom resource (CR) to manage communication with Agent components. Deploy the Principal component, provide the resource details to create the required secrets, and then restart the Principal component. The principal component uses a public key infrastructure (PKI) to secure all communications.

<div>

<div class="title">

Procedure

</div>

1.  Deploy the Argo CD instance with the Principal component enabled. The following example shows the configuration for enabling the Principal component in the Argo CD CR:

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: openshift-gitops
    spec:
      controller:
        enabled: false
      argoCDAgent:
        principal:
          enabled: true
          auth: "mtls:CN=([^,]+)"
          logLevel: "info"
          namespace:
            allowedNamespaces:
              - "*"
          tls:
            insecureGenerate: false
          jwt:
            insecureGenerate: false
      sourceNamespaces:
        - "agent-managed"
        - "agent-autonomous"
    ```

    where:

    `spec.argoCDAgent`
    Specifies the Argo CD Agent configuration.

    `spec.argoCDAgent.principal`
    Specifies the Principal component configuration.

    `spec.argoCDAgent.principal.auth`
    Specifies the authentication method used in the Principal component.

    `spec.argoCDAgent.principal.namespace`
    Specifies the namespace configuration used in the Principal component.

    `spec.argoCDAgent.principal.tls`
    Specifies the configuration used for secure communication.

    `spec.sourceNamespaces`
    Specifies the `sourceNamespaces` configuration.

    <div class="note">

    <div class="title">

    </div>

    - The namespace names specified in `sourceNamespaces` must exactly match the corresponding Agent names. If they do not match, the Principal cannot deploy or monitor applications on the spoke cluster in managed mode, or monitor applications on the spoke cluster in autonomous mode.

    - The Argo CD CR must be installed as a `cluster-scoped` Argo CD instance. See the *Additional Resources* section for how to install a `cluster-scoped` Argo CD instance.

    </div>

    1.  Apply the Argo CD resource to the hub cluster:

        ``` terminal
        $ oc apply -f argocd.yaml -n "<principal_namespace>" --context "<principal_context>"
        ```

        where:

        `principal_namespace`
        Specifies the namespace where the principal component is installed on the hub cluster.

        `principal_context`
        Specifies the context of the hub cluster where the principal component is running.

    2.  Verify Argo CD instance deployment. Check the pods in the principal namespace by running the following command.

        ``` terminal
        $ oc get pod -n "<principal_namespace>" --context "<principal_context>"
        ```

        Example output:

        ``` terminal
        NAME                                               READY  STATUS
        openshift-gitops-agent-principal-xxxxxxxxx-xxxxx   0/1    Running
        openshift-gitops-redis-xxxxxxxxx-xxxxx             1/1    Running
        openshift-gitops-repo-server-xxxxxxxxx-xxxxx       1/1    Running
        openshift-gitops-server-xxxxxxxxx-xxxxx            1/1    Running
        ```

        > [!IMPORTANT]
        > At this stage, Argo CD pods start successfully, but the principal pod remains in a `Running` (not Ready) state because the required secrets have not yet been created. You can create these secrets later, after the Red Hat OpenShift GitOps Operator enables the principal component, because some required values, such as the principal hostname and resource proxy service names, are only available at that point.

    3.  Verify the services created by the operator by running the following command:

        ``` terminal
        $ oc get svc -n "<principal_namespace>" --context "<principal_context>"
        ```

        Example output:

        ``` terminal
        NAME                                            TYPE      PORT(S)
        openshift-gitops-agent-principal                ClusterIP 443/TCP
        openshift-gitops-agent-principal-healthz        ClusterIP 8030/TCP
        openshift-gitops-agent-principal-metrics        ClusterIP 9000/TCP
        openshift-gitops-agent-principal-redisproxy     ClusterIP 6379/TCP
        openshift-gitops-agent-principal-resource-proxy ClusterIP 9090/TCP
        ```

    4.  By default, the Operator creates a route for the Principal, which is used to access Principal services. Verify the default route for the Principal component by running the following command:

        ``` terminal
        $ oc get route -n "<principal_namespace>" --context "<principal_context>"
        ```

        Example output:

        ``` terminal
        NAME                               HOST/PORT
        openshift-gitops-agent-principal   example-host-name
        ```

    5.  If you want to disable the route or use a `LoadBalancer` service, update the following section in the Argo CD resource:

        ``` yaml
        kind: ArgoCD
        spec:
          # (...)
          argocdAgent:
            principal:
              server:
                service:
                  type: LoadBalancer
                route:
                  enabled: false
        ```

2.  Create the required namespaces. You must create one namespace for each Agent that you plan to connect to the Principal. The namespace names must match the Agent names. Run the following commands:

    ``` terminal
    $ oc create namespace agent-managed --context "<principal_context>"
    $ oc create namespace agent-autonomous --context "<principal_context>"
    ```

    > [!NOTE]
    > Each Agent requires a dedicated namespace because Argo CD Agent architecture uses a **namespace-to-agent** mapping model. For managed Agents, the Principal sends applications only to those created in the corresponding Agent namespace on the hub cluster. Similarly, for autonomous Agents, applications are created in the respective Agent namespace at the hub.

3.  Ensure that the `AppProject` resource used for your Argo CD applications on the hub includes all Agent namespaces under the `.spec.sourceNamespaces` field, for example:

    ``` yaml
    spec:
      sourceNamespaces:
      - "agent-managed"
      - "agent-autonomous"
    ```

    1.  If you modify the `AppProject`, restart the Argo CD pods to apply the changes.

4.  Create required secrets.

    > [!IMPORTANT]
    > The CLI-generated PKI is intended for development and testing purposes only. For production environments, use certificates issued by your organization’s PKI or a trusted certificate authority.

    1.  Initialize the PKI

        1.  To initialize the certificate authority (CA) that signs other certificates, run the following command:

            ``` terminal
            $ argocd-agentctl pki init \
            --principal-namespace "<principal_namespace>" \
            --principal-context "<principal_context>"
            ```

            where:

            `principal_namespace`
            Specifies the namespace where the Principal component is installed.

            `principal_context`
            Specifies the context of the Principal component.

            This command generates a self-signed CA certificate and private key, and creates the `argocd-agent-ca` secret that contains the CA credentials. The CA is valid for signing certificates and includes a default expiration period.

        2.  To generate the server certificate for the Principal’s gRPC service, run the following command:

            ``` terminal
            $ argocd-agentctl pki issue principal \
                --principal-namespace "<principal_namespace>" \
                --principal-context "<principal_context>" \
                --dns "<principal_dns_name>"
            ```

            where:

            `principal-namespace`
            Specifies the namespace where the Principal component is installed.

            `principal-context`
            Specifies the context of the Principal component.

            `principal_dns_name`
            Specifies the hostname of the Principal service. Agents use this value to connect to the Principal’s gRPC service. This should match the `.spec.host` value of the Principal’s route, or `.status.loadBalancer.ingress.hostname` when the Principal service is of type `LoadBalancer`.

            `ip` (optional)
            Specifies the comma-separated list of IP addresses where the Principal component is accessible.

            `u`, `upsert` (optional)
            Updates the existing certificate if one already exists.

            This command issues a TLS certificate for the Principal to enable secure gRPC communication between the Principal and Agent components. It also creates the `argocd-agent-principal-tls` secret that contains the generated certificate and key.

        3.  Generate the server certificate for the resource proxy service by running the following command:

            ``` terminal
            $ argocd-agentctl pki issue resource-proxy \
                --principal-namespace "<principal_namespace>" \
                --principal-context "<principal_context>" \
                --dns "<resource_proxy_dns>"
            ```

            where:

            `principal-namespace`
            Specifies the namespace where the Principal component is installed.

            `principal-context`
            Specifies the context of the Principal component.

            `resource_proxy_dns`
            Specifies the service name for the `resource-proxy` in the hub cluster, for example, `<ArgoCD instance name>-agent-principal-resource-proxy`. Argo CD uses this service to connect to the `resource-proxy`. Because the Argo CD and the `resource-proxy` run in the same cluster, Argo CD can connect using the service name directly.

            `ip` (optional)
            Specifies the comma-separated list of IP addresses for the resource proxy that are reachable by the Argo CD API server.

            `u`, `upsert` (optional)
            Updates the existing certificate if one already exists.

            This command creates the `argocd-agent-resource-proxy-tls` secret that contains the TLS certificate for the resource proxy component. The certificate includes the required subject alternative names (SANs) for the resource proxy service and is signed by the same CA that was created during PKI initialization.

        4.  Generate the RSA private key by running the following command:

            ``` terminal
            $ argocd-agentctl jwt create-key \
                --principal-namespace "<principal_namespace>" \
                --principal-context "<principal_context>"
            ```

            where:

            `principal-namespace`
            Specifies the namespace where the Principal component is installed.

            `principal-context`
            Specifies the context of the Principal component.

            `u`, `upsert` (optional)
            Updates the existing JWT key if one already exists.

            This command generates a 4096-bit RSA private key in the `PKCS#8 PEM` format and stores it in the `argocd-agent-jwt` secret.

        5.  Verify that the corresponding secrets are created in the Principal namespace by running the following command:

            ``` terminal
            $ oc get secrets -n "<principal_namespace>" --context "<principal_context>" | grep agent
            ```

            Example output:

            ``` terminal
            NAME                               TYPE
            argocd-agent-ca                    kubernetes.io/tls
            argocd-agent-principal-tls         kubernetes.io/tls
            argocd-agent-resource-proxy-tls    kubernetes.io/tls
            argocd-agent-jwt                   Opaque
            ```

        6.  Verify that the principal component is now successfully started by running the following command:

            ``` terminal
            $ oc get pod -n "<principal_namespace>" --context "<principal_context>"
            ```

            Example output:

            ``` terminal
            NAME                                               READY  STATUS
            openshift-gitops-agent-principal-xxxxxxxxx-xxxxx   1/1    Running
            openshift-gitops-redis-xxxxxxxxx-xxxxx             1/1    Running
            openshift-gitops-repo-server-xxxxxxxxx-xxxxx       1/1    Running
            openshift-gitops-server-xxxxxxxxx-xxxxx            1/1    Running
            ```

        7.  Verify the pod logs in the Principal namespace by running the following command:

            ``` terminal
            $ oc logs "<principal_pod>" -n "<principal_namespace>" --context "<principal_context>"
            ```

            where:

            `principal_pod`
            Specifies the name of the principal pod running in the principal namespace. This pod hosts the principal component, which manages communication and certificate exchange with connected Agents.

            Example output:

            ``` terminal
            level=info msg="Starting metrics server on http://0.0.0.0:8000/metrics"
            level=info msg="Redis proxy started on 0.0.0.0:6379"
            level=info msg="Resource proxy started"
            level=info msg="Namespace informer synced and ready"
            level=info msg="Starting healthz server on :8003"
            ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Ensure that all Principal pods show a `Running` status and that the corresponding services and route are created. The Principal component is now ready to communicate securely with the Agent components on workload clusters. For more information on metrics exposed by the Principal component, see [Principal metrics, Argo CD upstream documentation](https://argocd-agent.readthedocs.io/latest/operations/metrics/#principal-metrics).

</div>

# Setting up a spoke cluster environment

After you configured the Principal component, you can connect it to one or more Agents. This connection allows the principal to securely manage Argo CD Applications on each Agent cluster.

<div>

<div class="title">

Prerequisites

</div>

- The Principal setup is complete and running.

- You have access to both the Principal and Agent clusters.

- The `argocd-agentctl` CLI tool is installed and accessible from your environment.

- The `helm` CLI is installed and configured. Ensure that the `helm` CLI version is later than v3.8.0.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the Agent secret on the Principal cluster by running the following command:

    ``` terminal
    $ argocd-agentctl agent create "<agent_name>" \
      --principal-context "<principal_context>" \
      --principal-namespace "<principal_namespace>" \
      --resource-proxy-server "<principal_resource_proxy_url>"
    ```

    where:

    `agent_name`
    A unique name used to identify each Agent managed by the Principal. The Agent CLI uses this value to create the Argo CD cluster secret (`cluster-<agent-name>`) and to construct the server URL.

    `principal-namespace`
    Specifies the namespace where the Principal component is installed.

    `principal-context`
    Specifies the cluster context of the Principal component.

    `principal_resource_proxy_url`
    Specifies the URL of the Principal resource-proxy, for example, `<ArgoCD Instance Name>-agent-principal-resource-proxy:9090`, which Argo CD uses to access live resources in the Agent’s cluster. In this model, Argo CD does not connect directly to the Agent cluster’s API server; rather, it sends requests to the Principal’s `resource-proxy`, which then forwards them to the appropriate Agent via gRPC.

    `label, l` (optional)
    Adds optional metadata labels for the Agent.

    This command generates a client certificate signed by the Principal CA, creates an Argo CD cluster secret with the certificate data and sets up credentials for resource proxy access.

2.  Copy the CA certificate to the Agent cluster by running the following command:

    ``` terminal
    $ argocd-agentctl pki propagate \
        --agent-context "<agent_context>" \
        --principal-context "<principal_context>" \
        --principal-namespace "<principal_namespace>" \
        --agent-namespace "<agent_namespace>"
    ```

    where:

    `principal-namespace`
    Specifies the namespace where the Principal component is installed.

    `agent-namespace`
    Specifies the namespace where the Agent component is installed.

    `principal-context`
    Specifies the kubeconfig context of the Principal (hub) cluster.

    `agent-context`
    Specifies the kubeconfig context of the Agent (workload) cluster.

    `force, f` (optional)
    Forces regeneration of the PKI if it already exists on the target cluster.

    This command copies the CA certificate from the Principal cluster and creates the `argocd-agent-ca` secret in the Agent cluster.

3.  Generate a client certificate for the Agent by running the following command:

    ``` terminal
    $ argocd-agentctl pki issue agent "<agent_name>" \
        --principal-context "<principal_context>" \
        --agent-context "<agent_context>" \
        --agent-namespace "<agent_namespace>" \
        --principal-namespace "<principal_namespace>"
    ```

    where:

    `principal-context`
    Specifies the kubeconfig context of the Principal (hub) cluster.

    `agent-context`
    Specifies the kubeconfig context of the Agent (workload) cluster.

    `agent-namespace`
    Specifies the namespace where the Agent component is installed.

    `principal-namespace`
    Specifies the namespace where the Principal component is installed.

    `upsert, u` (optional)
    Updates the existing JWT key if one already exists in the Agent namespace.

    This command creates the `argocd-agent-client-tls` secret, generates the Agent’s client certificate and private key, and signs the certificate using the Principal CA.

4.  Verify that all required secrets are created in the Agent namespace by running the following command:

    ``` terminal
    $ oc get secrets -n "<agent_namespace>" --context "<agent_context>" | grep agent
    ```

    Example output:

    ``` terminal
    NAME                              TYPE
    argocd-agent-ca                   kubernetes.io/tls
    argocd-agent-principal-tls        kubernetes.io/tls
    argocd-agent-resource-proxy-tls   kubernetes.io/tls
    argocd-agent-jwt                  Opaque
    ```

</div>

# Installing the Argo CD Agent by using a Helm chart

You can install the Argo CD Agent component on the workload cluster by using Helm charts. The Helm charts based installation process involves the following steps:

1.  Deploy an Argo CD instance on the Agent cluster.

2.  Install the Agent component using the Helm chart in one of the following modes:

    - **Managed mode**: The Principal manages the Agent configuration and lifecycle.

    - **Autonomous mode**: The Agent functions independently of the Principal.

## Deploying an Argo CD instance on the Agent cluster

Before you can install the Argo CD Agent using a Helm chart, you must deploy an Argo CD instance on the Agent cluster. This Argo CD instance runs alongside the Agent component and handles the application workloads on the workload cluster.

<div>

<div class="title">

Procedure

</div>

1.  Deploy an Argo CD instance on the Agent cluster by creating an Argo CD custom resource similar to the following example:

    ``` yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: openshift-gitops
    spec:
      server:
        enabled: false
    ```

2.  Apply the configuration by running the following command:

    ``` terminal
    $ oc apply -f argocd.yaml -n "<agent_namespace>" --context "<agent_context>"
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  To verify that the Argo CD instance is created, run the following command:

    ``` terminal
    $ oc get pod -n "<agent_namespace>" --context "<agent_context>"
    ```

    Example output:

    ``` terminal
    NAME                                           READY   STATUS
    openshift-gitops-application-controller-0      1/1     Running
    openshift-gitops-redis-5b6668544-sxtth         1/1     Running
    openshift-gitops-repo-server-8cb87b698-cnfgl   1/1     Running
    ```

</div>

## Installing the Argo CD Agent in managed mode by using a Helm chart

Use the Helm chart from the Argo CD Agent project to install the managed-mode Agent component on the workload cluster. In *managed mode*, the Agent must communicate with the spoke Redis server. However, the default network policy created by the Red Hat OpenShift GitOps Operator does not allow this communication.

<div>

<div class="title">

Procedure

</div>

1.  To enable communication, you must create a custom network policy by using the following YAML configuration.

    ``` yaml
    apiVersion: networking.k8s.io/v1
    kind: NetworkPolicy
    metadata:
      name: custom-agent-redis-network-policy
    spec:
      podSelector:
        matchLabels:
          app.kubernetes.io/name: <ArgoCD Instance Name>-redis
      ingress:
        - ports:
            - protocol: TCP
              port: 6379
          from:
            - podSelector:
                matchLabels:
                  app.kubernetes.io/name: redhat-argocd-agent
      policyTypes:
        - Ingress
    ```

    where:

    `spec.podSelector`
    Selects the pods this policy applies to, for example, the Redis pod labeled `app.kubernetes.io/name: <ArgoCD Instance Name>-redis`.

    `spec.ingress`
    Defines the allowed inbound traffic rules for the selected pods.

    `spec.policyTypes`
    Indicates that this policy is an Ingress policy, meaning it only checks incoming connections.

    1.  Apply the network policy by using the following command:

        ``` terminal
        $ oc apply -f network-policy.yaml -n "<agent_namespace>" --context "<agent_context>"
        ```

        where:

        `agent_namespace`
        Specifies the namespace where the network policy is created.

        `agent_context`
        Ensures that the command runs against the Agent cluster and not on the hub cluster.

2.  Add the OpenShift Container Platform Helm chart repository by running the following command:

    ``` terminal
    $ helm repo add openshift-helm-charts https://charts.openshift.io/
    ```

3.  Install the managed Agent using Helm by using the following command:

    ``` terminal
    $ helm install redhat-argocd-agent openshift-helm-charts/redhat-argocd-agent \
    --version <chart_version> \
    --set namespaceOverride=<agent_namespace> \
    --set agentMode="managed" \
    --set server="<principal_route_dns>" \
    --set argoCdRedisSecretName="<argocd_name>-redis-initial-password" \
    --set argoCdRedisPasswordKey="admin.password" \
    --set redisAddress="<argocd_name>-redis:6379" \
    --kube-context "<agent_context>"
    ```

    where:

    `namespaceOverride`
    Overrides the default namespace in which the Agent is installed. Set this to the namespace created for the Agent on the managed (spoke) cluster. Ensure the namespace exists before installation unless using the Helm namespace creation flags.

    `agentMode`
    Defines how the Agent operates.

    - `managed`: The Principal manages the Agent configuration and lifecycle.

    - `autonomous`: The Agent functions independently of the Principal.

    `server`
    Specifies the hostname of the Principal service. Agents use this value to connect to the Principal’s gRPC service. This should match either:

    - The `.spec.host` value of the Principal route (when using OpenShift Routes), or

    - The `.status.loadBalancer.ingress.hostname` of the Principal service (when using a LoadBalancer service type). This value must be reachable *from the Agent cluster*, and DNS resolution must work across clusters.

    `argoCdRedisSecretName`
    The name of the Kubernetes Secret in the Agent namespace that contains the Redis password for the Argo CD instance running on the Agent cluster. This must match the secret created by the Argo CD installation.

    `argoCdRedisPasswordKey`
    The key within the Secret specified in `argoCdRedisSecretName` that stores the Redis password. This is usually `admin.password` for Red Hat OpenShift GitOps deployments.

    `redisAddress`
    The host and port of the Redis instance associated with the Agent’s Argo CD installation. Typically formatted as `<argocd_name>-redis:6379`. Ensure the Redis Service name and port match the installed Argo CD instance.

    `kube-context`
    The kubeconfig context of the **Agent (managed)** cluster. The Helm install runs against this context, so it must point to the correct remote cluster configured for the Agent.

</div>

## Installing the Argo CD Agent in autonomous mode by using a Helm chart

Use the Helm chart provided by the Argo CD Agent project to install the autonomous mode Agent component on the spoke (workload) cluster. In **autonomous** mode, the Agent must communicate with the spoke Redis server. However, the default network policy created by the Red Hat OpenShift GitOps Operator does not allow this communication.

<div>

<div class="title">

Procedure

</div>

1.  To enable communication, you must create a custom network policy by using the following YAML configuration.

    ``` yaml
    apiVersion: networking.k8s.io/v1
    kind: NetworkPolicy
    metadata:
      name: custom-agent-redis-network-policy
    spec:
      podSelector:
        matchLabels:
          app.kubernetes.io/name: <ArgoCD Instance Name>-redis
      ingress:
        - ports:
            - protocol: TCP
              port: 6379
          from:
            - podSelector:
                matchLabels:
                  app.kubernetes.io/name: redhat-argocd-agent
      policyTypes:
        - Ingress
    ```

    where:

    `spec.podSelector`
    Selects the pods this policy applies to, for example, the Redis pod labeled `app.kubernetes.io/name: <ArgoCD Instance Name>-redis`.

    `spec.ingress`
    Defines the allowed inbound traffic rules for the selected pods.

    `spec.policyTypes`
    Indicates that this policy is an Ingress policy, meaning it only checks incoming connections.

2.  Apply the network policy by using the following command:

    ``` terminal
    $ oc apply -f network-policy.yaml -n "<agent_namespace>" --context "<agent_context>"
    ```

    where:

    `<agent_namespace>`
    Specifies the namespace where the Agent instance is deployed. Use this value to specify the target namespace when you apply the network policy.

    `<agent_context>`
    Specifies the context for the cluster that runs the Agent instance. Use this value to ensure that the command is executed on the correct cluster when multiple contexts are configured.

3.  Add the OpenShift Container Platform Helm chart repository by running the following command:

    ``` terminal
    $ helm repo add openshift-helm-charts https://charts.openshift.io/
    ```

4.  Install the autonomous Agent using Helm by using the following command:

    ``` terminal
    $ helm install argocd-agent openshift-helm-charts/redhat-argocd-agent \
    --version "<chart_version>" \
    --set namespaceOverride=<agent_namespace> \
    --set agentMode="autonomous" \
    --set server="<principal_route_dns>" \
    --set argoCdRedisSecretName="<argocd_name>-redis-initial-password" \
    --set argoCdRedisPasswordKey="admin.password" \
    --set redisAddress="<argocd_name>-redis:6379" \
    --kube-context "<agent_context>"
    ```

    where:

    `<chart_version>`
    Specifies the version of the `redhat-argocd-agent` Helm chart that you want to install.

    `<agent_namespace>`
    Defines the namespace where the Argo CD Agent component will be installed on the spoke cluster.

    `<agent_context>`
    Defines the `kube-context` for the spoke cluster where the Agent is deployed.

    `<principal_route_dns>`
    Specifies the hostname of the Principal service. Agents use this value to connect to the Principal’s gRPC service. This should match the `.spec.host` value of the Principal’s route, or `.status.loadBalancer.ingress.hostname` when the Principal service is of type `LoadBalancer`.

    `<argocd_name>`
    Specifies the name of the Argo CD instance installed alongside the Agent. This value is used to construct Redis-related resource names.

    `<argocd_name>-redis-initial-password`
    Defines the name of the Kubernetes secret that stores the initial Redis password for the Argo CD instance.

5.  Create an `AppProject` in the agent namespace.

    ``` yaml
    apiVersion: argoproj.io/v1alpha1
    kind: AppProject
    metadata:
      name: default
      namespace: <agent_namespace>
    spec:
      clusterResourceWhitelist:
      - group: '*'
        kind: '*'
      destinations:
      - name: '*'
        namespace: '*'
        server: '*'
      sourceRepos:
      - '*'
    ```

    For more information, see the *Additional Resources* section, which includes the upstream documentation link on creating `AppProject` resources in Agents.

</div>

# Installing the Argo CD Agent by using an Argo CD custom resource

After you create the required secrets, deploy the Agent component. You can install the Argo CD Agent in the spoke cluster by defining an Argo CD custom resource (CR).

Use the following information to install the Agent component in either the **Managed** or the **Autonomous** mode.

<div>

<div class="title">

Prerequisites

</div>

- The required secrets for the Agent component are created.

- You have access to the cluster with sufficient permissions to apply custom resources.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create or update the Argo CD custom resource to enable the Agent component.

    1.  To enable the **Managed** Agent mode, use the following configuration:

        ``` yaml
        apiVersion: argoproj.io/v1beta1
        kind: ArgoCD
        metadata:
          name: openshift-gitops
        spec:
          server:
            enabled: false
          argoCDAgent:
            agent:
              enabled: true
              client:
                keepAliveInterval: 50s
                mode: managed
                principalServerAddress: "<principal_route_dns>"
                principalServerPort: "443"
              logLevel: "info"
              creds: "mtls:any"
              redis:
                serverAddress: "<argocd_name>-redis:6379"
              tls:
                insecure: false
                rootCASecretName: argocd-agent-ca
                secretName: argocd-agent-client-tls
        ```

    2.  To enable the **Autonomous** Agent mode, use the following configuration:

        ``` yaml
        apiVersion: argoproj.io/v1beta1
        kind: ArgoCD
        metadata:
          name: openshift-gitops
        spec:
          server:
            enabled: false
          argoCDAgent:
            agent:
              enabled: true
              client:
                keepAliveInterval: 50s
                mode: autonomous
                principalServerAddress: "<principal_route_dns>"
                principalServerPort: "443"
              logLevel: "info"
              creds: "mtls:any"
              redis:
                serverAddress: "<argocd_name>-redis:6379"
              tls:
                insecure: false
                rootCASecretName: argocd-agent-ca
                secretName: argocd-agent-client-tls
        ```

        where:

        `principal_route_dns`
        specifies the hostname of the Principal service. Agents use this value to connect to the Principal gRPC service. This value must match the `.spec.host` field of the Principal route or the `.status.loadBalancer.ingress.hostname` field when the Principal service is exposed as a `LoadBalancer`.

        `argocd_name`
        specifies the name of the Argo CD instance.

        `agent_namespace`
        specifies the namespace where the Agent is deployed.

        `agent_context`
        specifies the kubeconfig context for the spoke cluster.

        > [!NOTE]
        > The Argo CD custom resource must be installed as a **cluster-scoped** Argo CD instance. For more information, see the *Additional Resources* section for how to install a cluster-scoped Argo CD instance.

    3.  If you use the **Autonomous** agent mode, you must create an `AppProject` in the agent namespace.

        ``` yaml
        apiVersion: argoproj.io/v1alpha1
        kind: AppProject
        metadata:
          name: default
          namespace: <agent_namespace>
        spec:
          clusterResourceWhitelist:
          - group: '*'
            kind: '*'
          destinations:
          - name: '*'
            namespace: '*'
            server: '*'
          sourceRepos:
          - '*'
        ```

        For more information, see the *Additional Resources* section, which includes the upstream documentation link on creating `AppProject` resources in Agents.

2.  Apply the Argo CD custom resource to the spoke cluster by running the following command:

    ``` terminal
    $ oc apply -f argocd.yaml -n "<agent_namespace>" --context "<agent_context>"
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the Argo CD instance and Agent components are deployed successfully by running the following command:

    ``` terminal
    $ oc get pods -n "<agent_namespace>" --context "<agent_context>"
    ```

    Example output:

    ``` terminal
    NAME                                            READY   STATUS
    openshift-gitops-agent-agent-xxxxxxxxx-xxxxx    1/1     Running
    openshift-gitops-application-controller-0       1/1     Running
    openshift-gitops-redis-xxxxxxxxx-xxxxx          1/1     Running
    openshift-gitops-repo-server-xxxxxxxxx-xxxxx    1/1     Running
    ```

</div>

# Verifying the Argo CD Agent installation in Managed mode or Autonomous mode

To verify that the Argo CD Agent is correctly installed and connected to the Principal cluster in managed or autonomous mode, complete the following steps.

<div>

<div class="title">

Procedure

</div>

1.  Verify that the Agent deployment is created by running the following command:

    ``` terminal
    $ oc get pod -n "<agent_namespace>" --context "<agent_context>"
    ```

    Example output:

    ``` terminal
    NAME                                           READY   STATUS
    argocd-agent-agent-6489fc5dd-48whw             1/1     Running
    ```

2.  To verify that the Agent component is successfully connected with Principal, run the following command:

    ``` terminal
    $ oc logs "<agent_pod>" -n "<agent_namespace>" --context "<agent_context>"
    ```

    As a result, the following messages are displayed in the pod logs.

    ``` terminal
    level=info msg="Authentication successful"
    level=info msg="Connected to argocd-agent-0.0.1-alpha"
    level=info msg="Starting event writer"
    level=info msg="Starting to send events to event stream"
    level=info msg="Starting to receive events from event stream"
    ```

3.  (Optional) Verify that the Agent metrics service is available. The Agent starts a metrics server exposed through a ClusterIP service, for example: `openshift-gitops-agent-agent-metrics`. You can create a route to expose this service externally.

4.  Verify the connection from the Principal cluster.

    1.  On the Principal cluster, check the logs of the Principal pod by running the following command:

        ``` terminal
        $ oc logs "<principal_pod>" --tail 10 -n "<principal_namespace>" --context "<principal_context>"
        ```

        Confirm that the following log messages are displayed:

        ``` terminal
        level=info msg="An agent connected to the subscription stream"
        level=info msg="Updated connection status to 'Successful' in Cluster: '<agent_name>' mapped with Agent: '<agent_name>'"
        level=info msg="Starting event writer"
        ```

    2.  (Optional) Verify the Principal metrics endpoint, a successful connection increases the metric `agent_connected_with_principal` by number of agents connected to the hub.

    3.  To list connected Agents, run the following command:

        ``` terminal
        $ argocd-agentctl agent list --principal-namespace "<principal_namespace>" --principal-context "<principal_context>"
        ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that all Agent pods are in the `Running` state and that secrets and Helm deployments have been successfully created before proceeding with synchronization.

</div>

# Deploying Argo CD applications

You can deploy Argo CD Applications using either the managed agent mode or the autonomous agent mode. The deployment mode determines which mode is the source of truth and where the Argo CD application must be created.

- In managed agent mode, the **hub cluster** is the source of truth.

- In autonomous agent mode, the **spoke cluster** is the source of truth.

## Deploying an Argo CD application in managed mode

In managed agent mode, the **hub** acts as the source of truth. Argo CD applications must be created in the hub cluster. The agent creates and manages the application in the spoke cluster based on the configuration defined in the hub.

<div>

<div class="title">

Prerequisites

</div>

- You have deployed and configured the Principal and Agent component.

- You have the `oc` CLI installed and are logged in with sufficient permissions.

- You know the context names for both the hub (control plane) and spoke (workload) clusters.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the Argo CD application manifest file, `application.yaml`, with the following configuration:

    ``` yaml
    apiVersion: argoproj.io/v1alpha1
    kind: Application
    metadata:
      name: my-demo-app
      namespace: agent-managed
    spec:
      project: default
      source:
        repoURL: https://github.com/redhat-developer/openshift-gitops-getting-started
        targetRevision: HEAD
        path: app
      destination:
        name: agent-managed
        namespace: my-app
      syncPolicy:
        automated:
          prune: true
          selfHeal: true
        managedNamespaceMetadata:
          labels:
            argocd.argoproj.io/managed-by: openshift-gitops
        syncOptions:
        - CreateNamespace=true
    ```

    where:

    `metadata.name`
    Specifies the name of the Agent cluster on the hub.

    `metadata.namespace`
    Specifies the namespace on the principal cluster where the Agent’s managed applications are stored.

2.  Apply the configuration in the hub cluster by running the following command:

    ``` terminal
    $ oc apply -f application.yaml -n agent-managed --context "<principal_context>"
    ```

    where:

    `principal_context`
    Specifies the context that points to the hub cluster where the Principal component is running.

</div>

<div>

<div class="title">

Verification

</div>

1.  To verify that the application is created in the spoke cluster, run the following command:

    ``` terminal
    $ oc get application.argoproj.io/my-demo-app -n openshift-gitops --context "<agent_context>"
    ```

    where:

    `agent_context`
    Specifies the context that points to the Agent cluster where the Agent component is running.

2.  To verify that the application is synced and healthy from the hub, run the following command:

    ``` terminal
    $ oc get application.argoproj.io/my-demo-app -n agent-managed --context "<principal_context>"
    ```

    where:

    `principal_context`
    Specifies the context that points to the hub cluster where the Principal component is running.

3.  If the configuration is correct, the Agent creates the application and its associated resources in the spoke cluster. Because the hub is the source of truth, any direct changes made in the spoke cluster are automatically reverted by the Agent component.

</div>

## Deploying an Argo CD application in autonomous mode

In autonomous agent mode, the **spoke** acts as the source of truth. The Argo CD applications must be created directly in the spoke cluster, and the agent reports the application state back to the Principal component in the hub.

<div>

<div class="title">

Prerequisites

</div>

- You have deployed and configured the Principal and Agent component.

- You have the `oc` CLI installed and are logged in with sufficient permissions.

- You know the context names for both the hub (control plane) and spoke (workload) clusters.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the Argo CD application manifest file, `application.yaml`, with the following configuration:

    ``` yaml
    apiVersion: argoproj.io/v1alpha1
    kind: Application
    metadata:
      name: my-demo-app
      namespace: openshift-gitops
    spec:
      project: default
      source:
        repoURL: https://github.com/redhat-developer/openshift-gitops-getting-started
        targetRevision: HEAD
        path: app
      destination:
        server: https://kubernetes.default.svc
        namespace: my-app
      syncPolicy:
        automated:
          prune: true
          selfHeal: true
        managedNamespaceMetadata:
          labels:
            argocd.argoproj.io/managed-by: openshift-gitops
        syncOptions:
        - CreateNamespace=true
    ```

    where:

    `metadata.namespace`
    Specifies the namespace where the Argo CD instance (Agent) is running on the spoke cluster. This controller manages the Application resource.

    `source.repoURL`
    Specifies the Git repository that stores the application manifests.

    `source.targetRevision`
    Specifies the Git revision Argo CD should track.

    `source.path`
    Specifies the directory inside the repository containing the application manifests.

    `destination.server`
    Specifies the Kubernetes API server where the application will be deployed.

    `destination.namespace: my-app`
    Specifies the target namespace for the deployed application. If the namespace does not exist, it can be automatically created.

    `syncPolicy.automated.prune`
    Enables automated pruning. Argo CD deletes resources that were previously applied but no longer appear in Git.

    `syncPolicy.automated.selfHeal`
    Enables automatic self-healing. Argo CD corrects any drift between live resources and the Git source.

    `managedNamespaceMetadata.labels`
    Labels that Argo CD applies to the destination namespace when it creates or manages it. The label in this example indicates the namespace is managed by the `openshift-gitops` instance.

2.  Apply the configuration in the spoke cluster by running the following command:

    ``` terminal
    $ oc apply -f application.yaml -n openshift-gitops --context "<agent_context>"
    ```

    where:

    `agent_context`
    Specifies the context name for the agent cluster in an Agent-Principal setup.

</div>

<div>

<div class="title">

Verification

</div>

1.  To verify that the application is created in the hub cluster, run the following command:

    ``` terminal
    $ oc get application.argoproj.io/my-demo-app -n agent-autonomous --context "<principal_context>"
    ```

    where:

    `principal_context`
    Specifies the context name for the principal cluster in an Agent-Principal setup.

2.  To verify that the application is synced and healthy from the spoke, run the following command:

    ``` terminal
    $ oc get application.argoproj.io/my-demo-app -n openshift-gitops --context "<agent_context>"
    ```

3.  If the configuration is correct, the agent creates all application resources in the spoke cluster. As the spoke cluster is the source of truth, direct changes in the hub cluster are not allowed.

</div>

# Troubleshooting Principal-Agent communication and deployment issues

Use the following troubleshooting steps if you encounter issues during Principal-Agent communication or application deployment.

Agent cannot connect to the Principal
This issue can occur for one or more of the following reasons:

- The Principal or Agent pods are not healthy.

- The hostname of the principal, exposed via Route in the Agent Helm chart (`server` parameter in the `values.yaml` file or the `--set server` flag) is incorrect.

- Required certificates or secrets were not created correctly.

To resolve this issue:

- Verify that the Principal and Agent pods are running and healthy.

- Confirm that the `server` parameter in the Agent Helm chart matches the hostname of the principal, exposed via Route.

- Check that the certificates and secrets required for Principal-Agent communication exist in the correct namespaces.

Agent cannot connect to Redis
You see the following connection error messages in agent pod logs:

``` terminal
redis: connection pool: failed to dial after 2 attempts: dial tcp xxx.xx.xx.xxx:6379: i/o timeout
level=error msg="Failed to get cluster info from cache" error="dial tcp 172.30.60.217:6379: i/o timeout" event=addClusterCacheInfoUpdateToQueue module=Agent
level=error msg="Failed to get cluster info from cache" error="NOAUTH Authentication required." event=addClusterCacheInfoUpdateToQueue module=Agent
```

This issue can occur if one or more of the following conditions are true:

- The Redis pod is not healthy.

- The Redis address specified in the Agent Helm chart (`redisAddress` in `values.yaml` or the `--set redisAddress` flag) is incorrect.

- The Redis secret name (`argoCdRedisSecretName`) is incorrect or the secret does not exist in the Agent’s namespace.

- The key name containing the Redis password (`argoCdRedisPasswordKey`) is incorrect or missing from the secret.

- The Redis service is not accessible due to namespace or networking restrictions.

- A `NetworkPolicy` is blocking API calls from the Agent to Redis.

To resolve this issue:

- Verify that the Redis pod is running and healthy.

- Check that the Redis service and secret configuration in the Helm chart match the expected values.

- Ensure that no `NetworkPolicy` objects are preventing communication between the Agent and Redis.

Agent handshake with Principal fails
You might see the following warning in the Agent pod logs:

``` terminal
level=warning msg="Auth failure: rpc error: code = Unavailable desc = connection error: desc = \"transport: authentication handshake failed: tls: failed to verify certificate: x509: certificate is valid for openshift-gitops-agent-principal--generated, not openshift-gitops-agent-principal-argocd.apps.dcrs-h.ocp-dhte-citc.com\" (retrying in 1.44s)"
```

This failure usually occurs when:

- The Principal component automatically generates insecure TLS certificates (`.spec.argoCDAgent.principal.tls.insecureGenerate: true`).

- The Agent is configured to validate certificates (`tlsClientInSecure` is set to `false` in the Helm install command).

To resolve this issue, perform one of the following actions:

- Disable certificate validation at the Agent by setting `tlsClientInSecure=true`.

  > [!WARNING]
  > The `tlsClientInSecure=true` setting disables TLS verification and is insecure. Do not use it in production environments.

- Disable automatic certificate generation at the Principal component by setting `insecureGenerate: false`.

Agent cannot view Workload Cluster resources
You might view the following error in the Argo CD Web UI:

``` terminal
Resource not found in cluster: apps/v1/Deployment:(resource-name)
Please update your resource specification to use the latest Kubernetes API resources supported by the target cluster. The recommended syntax is apps/v1/Deployment:guestbook-ui
```

In addition, you might view the following error in the Managed or Autonomous Agent pod logs:

``` terminal
time="(...)" level=error msg="could not request resource: pods \"(...)\" is forbidden: User \"system:serviceaccount:argocd:argocd-agent-agent\" cannot get resource \"pods\" in API group \"\" in the namespace \"guestbook\"" method=processIncomingResourceRequest
```

These errors occurs when the Argo CD Agent does not have the necessary permissions to view resources outside the namespace in which it is installed. To resolve this issue, ensure that the Agent has appropriate access to the required namespace.

# Additional resources

- [Argo CD Agent architecture overview](../argo_cd_agent_architecture/argocd-agent-architecture-overview.md)

- [Apps in any namespaces](../argocd_applications/managing-apps-in-non-control-plane-namespaces.md)

- [cluster-scoped Argo CD instance](../declarative_clusterconfig/configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.md#using-argo-cd-instance-to-manage-cluster-scoped-resources_configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations)

[argocd-agentctl CLI tool](https://developers.redhat.com/content-gateway/rest/browse/pub/cgw/openshift-gitops)

- [Helm CLI (Argo CD Agent upstream documentation)](https://helm.sh/docs/intro/install/)

- [Principal Component Configuration section (Argo CD Agent upstream documentation)](https://argocd-agent.readthedocs.io/latest/configuration/principal/configuration/)

- [Agent Component Configuration section (Argo CD Agent upstream documentation)](https://argocd-agent.readthedocs.io/latest/configuration/agent/configuration/)

- [Creating AppProjects for Agents (Argo CD Agent upstream documentation)](https://argocd-agent.readthedocs.io/latest/user-guide/appprojects/)
