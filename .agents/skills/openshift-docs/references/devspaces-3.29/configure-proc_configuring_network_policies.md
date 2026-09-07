> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_configuring_network_policies). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Restrict network traffic between workspaces

Restrict traffic between workspace Pods in different user projects by configuring network policies for multitenant isolation. By default, all Pods in an OpenShift cluster can communicate across namespaces.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have an OpenShift cluster with network restrictions such as multitenant isolation.

## About this task

With multitenant isolation, NetworkPolicy objects restrict all incoming traffic to Pods in a user project. However, Pods in the OpenShift Dev Spaces project must still communicate with Pods in user projects.

## Procedure

1.  Create an `allow-from-openshift-devspaces.yaml` file. The `allow-from-openshift-devspaces` NetworkPolicy allows incoming traffic from the OpenShift Dev Spaces namespace to all Pods in the user project.

    ``` yaml
    apiVersion: networking.k8s.io/v1
    kind: NetworkPolicy
    metadata:
        name: allow-from-openshift-devspaces
    spec:
        ingress:
        - from:
            - namespaceSelector:
                matchLabels:
                    kubernetes.io/metadata.name: openshift-devspaces
        podSelector: {}
        policyTypes:
        - Ingress
    ```

    where:

    `kubernetes.io/metadata.name: openshift-devspaces`  
    Selects traffic from the OpenShift Dev Spaces namespace. The default namespace is `openshift-devspaces`.

    `podSelector: {}`  
    The empty `podSelector` selects all Pods in the project.

2.  Apply the `allow-from-openshift-devspaces` NetworkPolicy to each user project:

    ``` bash
    oc apply -f allow-from-openshift-devspaces.yaml -n <user_namespace>
    ```

3.  Optional: If you configured [multitenant isolation with network policy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_security/network-policy#multitenant-network-policy), create and apply the `allow-from-openshift-apiserver` and `allow-from-workspaces-namespaces` NetworkPolicies to `openshift-devspaces`. The `allow-from-openshift-apiserver` NetworkPolicy allows incoming traffic from the `openshift-apiserver` namespace to the `devworkspace-webhook-server`, enabling webhooks. The `allow-from-workspaces-namespaces` NetworkPolicy allows incoming traffic from each user project to the `che-gateway` pod.
    1.  Create an `allow-from-openshift-apiserver.yaml` file:

        ``` yaml
        apiVersion: networking.k8s.io/v1
        kind: NetworkPolicy
        metadata:
          name: allow-from-openshift-apiserver
          namespace: openshift-devspaces
        spec:
          podSelector:
            matchLabels:
              app.kubernetes.io/name: devworkspace-webhook-server
          ingress:
            - from:
                - podSelector: {}
                  namespaceSelector:
                    matchLabels:
                      kubernetes.io/metadata.name: openshift-apiserver
          policyTypes:
            - Ingress
        ```

        where:

        `namespace: openshift-devspaces`  
        The OpenShift Dev Spaces namespace. The default is `openshift-devspaces`.

        `app.kubernetes.io/name: devworkspace-webhook-server`  
        The `podSelector` only selects devworkspace-webhook-server pods.

    2.  Create an `allow-from-workspaces-namespaces.yaml` file:

        ``` yaml
        apiVersion: networking.k8s.io/v1
        kind: NetworkPolicy
        metadata:
          name: allow-from-workspaces-namespaces
          namespace: openshift-devspaces
        spec:
          podSelector: {}
          ingress:
            - from:
                - podSelector: {}
                  namespaceSelector:
                    matchLabels:
                      app.kubernetes.io/component: workspaces-namespace
          policyTypes:
            - Ingress
        ```

        where:

        `namespace: openshift-devspaces`  
        The OpenShift Dev Spaces namespace. The default is `openshift-devspaces`.

        `podSelector: {}`  
        The empty `podSelector` selects all pods in the OpenShift Dev Spaces namespace.

    3.  Apply both NetworkPolicies:

        ``` bash
        oc apply -f allow-from-openshift-apiserver.yaml -n openshift-devspaces
        oc apply -f allow-from-workspaces-namespaces.yaml -n openshift-devspaces
        ```

## Results

- Verify that the NetworkPolicy is applied in the user namespace:

  ``` bash
  oc get networkpolicy -n <user_namespace>
  ```

- Start a workspace and verify that the workspace can communicate with the OpenShift Dev Spaces server.

**Related information**  

- [How workspace namespaces are organized](configure-con_configuring_projects.md)
- [Network isolation](https://kubernetes.io/docs/concepts/security/multi-tenancy/#network-isolation)
- [Configuring multitenant isolation with network policy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_security/network-policy#multitenant-network-policy)
