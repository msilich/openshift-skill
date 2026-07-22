<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

After installing OpenShift Container Platform, you can further expand and customize your network to your requirements.

# Using the Cluster Network Operator

You can use the Cluster Network Operator (CNO) to deploy and manage cluster network components on an OpenShift Container Platform cluster, including the Container Network Interface (CNI) network plugin selected for the cluster during installation.

For more information, see [Cluster Network Operator in OpenShift Container Platform](../networking/networking_operators/cluster-network-operator.md#nw-cluster-network-operator_cluster-network-operator).

# Network configuration tasks

- [Configuring the cluster-wide proxy](../networking/configuring_network_settings/enable-cluster-wide-proxy.md#enable-cluster-wide-proxy)

- [Configuring ingress cluster traffic overview](../networking/ingress_load_balancing/configuring_ingress_cluster_traffic/overview-traffic.md#overview-traffic)

- [Configuring the node port service range](../networking/configuring_network_settings/configuring-node-port-service-range.md#configuring-node-port-service-range)

- [Configuring IPsec encryption](../networking/network_security/configuring-ipsec-ovn.md#configuring-ipsec-ovn)

- [Create a network policy](../networking/network_security/network_policy/creating-network-policy.md#creating-network-policy) or [configure multitenant isolation with network policies](../networking/network_security/network_policy/multitenant-network-policy.md#multitenant-network-policy)

- [Optimizing routing](../scalability_and_performance/optimization/routing-optimization.md#routing-optimization)

- [Understanding multiple networks](../networking/multiple_networks/understanding-multiple-networks.md#understanding-multiple-networks)

## Creating default network policies for a new project

As a cluster administrator, you can modify the new project template to automatically include `NetworkPolicy` objects when you create a new project.

### Modifying the template for new projects

To modify the default project template to customize the resources and settings applied when users create new projects, you can create a custom project template.

As a cluster administrator, you can modify the default project template so that new projects are created using your custom requirements.

To create your own custom project template:

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in as a user with `cluster-admin` privileges.

2.  Generate the default project template:

    ``` terminal
    $ oc adm create-bootstrap-project-template -o yaml > template.yaml
    ```

3.  Use a text editor to modify the generated `template.yaml` file by adding objects or modifying existing objects.

4.  The project template must be created in the `openshift-config` namespace. Load your modified template:

    ``` terminal
    $ oc create -f template.yaml -n openshift-config
    ```

5.  Edit the project configuration resource using the web console or CLI.

    - Using the web console:

      1.  Navigate to the **Administration** → **Cluster Settings** page.

      2.  Click **Configuration** to view all configuration resources.

      3.  Find the entry for **Project** and click **Edit YAML**.

    - Using the CLI:

      1.  Edit the `project.config.openshift.io/cluster` resource:

          ``` terminal
          $ oc edit project.config.openshift.io/cluster
          ```

6.  Update the `spec` section to include the `projectRequestTemplate` and `name` parameters, and set the name of your uploaded project template. The default name is `project-request`.

    <div class="formalpara">

    <div class="title">

    Project configuration resource with custom project template

    </div>

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: Project
    metadata:
    # ...
    spec:
      projectRequestTemplate:
        name: <template_name>
    # ...
    ```

    </div>

7.  After you save your changes, create a new project to verify that your changes were successfully applied.

</div>

### Adding network policies to the new project template

You can add `NetworkPolicy` objects to the default project template so that new projects automatically include predefined network isolation rules. Applying network policies through templates helps enforce consistent network security controls across projects.

<div>

<div class="title">

Prerequisites

</div>

- Your cluster uses a default container network interface (CNI) network plugin that supports `NetworkPolicy` objects, such as the OVN-Kubernetes.

- You installed the OpenShift CLI (`oc`).

- You must log in to the cluster with a user with `cluster-admin` privileges.

- You must have created a custom default project template for new projects.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the default template for a new project by running the following command:

    ``` terminal
    $ oc edit template <project_template> -n openshift-config
    ```

    Replace `<project_template>` with the name of the default template that you configured for your cluster. The default template name is `project-request`.

2.  In the template, add each `NetworkPolicy` object as an element to the `objects` parameter. The `objects` parameter accepts a collection of one or more objects.

    In the following example, the `objects` parameter collection includes several `NetworkPolicy` objects.

    ``` yaml
    objects:
    - apiVersion: networking.k8s.io/v1
      kind: NetworkPolicy
      metadata:
        name: allow-from-same-namespace
      spec:
        podSelector: {}
        ingress:
        - from:
          - podSelector: {}
    - apiVersion: networking.k8s.io/v1
      kind: NetworkPolicy
      metadata:
        name: allow-from-openshift-ingress
      spec:
        ingress:
        - from:
          - namespaceSelector:
              matchLabels:
                policy-group.network.openshift.io/ingress:
        podSelector: {}
        policyTypes:
        - Ingress
    - apiVersion: networking.k8s.io/v1
      kind: NetworkPolicy
      metadata:
        name: allow-from-kube-apiserver-operator
      spec:
        ingress:
        - from:
          - namespaceSelector:
              matchLabels:
                kubernetes.io/metadata.name: openshift-kube-apiserver-operator
            podSelector:
              matchLabels:
                app: kube-apiserver-operator
        policyTypes:
        - Ingress
    ...
    ```

3.  Optional: Create a new project and confirm the successful creation of your network policy objects.

    1.  Create a new project:

        ``` terminal
        $ oc new-project <project>
        ```

        Replace `<project>` with the name of the project you want to create.

    2.  Confirm that the network policy objects in the new project template exist in the new project:

        ``` terminal
        $ oc get networkpolicy
        ```

        Expected output:

        ``` terminal
        NAME                           POD-SELECTOR   AGE
        allow-from-openshift-ingress   <none>         7s
        allow-from-same-namespace      <none>         7s
        ```

</div>
