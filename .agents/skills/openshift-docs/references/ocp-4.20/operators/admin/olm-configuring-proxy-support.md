<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

If a global proxy is configured on your OpenShift Container Platform cluster, Operator Lifecycle Manager (OLM) automatically configures Operators that it manages with the cluster-wide proxy. However, you can also configure installed Operators to override the global proxy or inject a custom CA certificate.

<div>

<div class="title">

Additional resources

</div>

- [Configuring the cluster-wide proxy](../../networking/configuring_network_settings/enable-cluster-wide-proxy.md#enable-cluster-wide-proxy)

</div>

- [Configuring a custom PKI](../../networking/configuring_network_settings/configuring-a-custom-pki.md#configuring-a-custom-pki) (custom CA certificate)

# Overriding proxy settings of an Operator

If a cluster-wide egress proxy is configured, Operators running with Operator Lifecycle Manager (OLM) inherit the cluster-wide proxy settings on their deployments. Cluster administrators can also override these proxy settings by configuring the subscription of an Operator.

> [!IMPORTANT]
> Operators must handle setting environment variables for proxy settings in the pods for any managed Operands.

<div>

<div class="title">

Prerequisites

</div>

- Access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate in the web console to the **Ecosystem → Software Catalog** page.

2.  Select the Operator and click **Install**.

3.  On the **Install Operator** page, modify the `Subscription` object to include one or more of the following environment variables in the `spec` section:

    - `HTTP_PROXY`

    - `HTTPS_PROXY`

    - `NO_PROXY`

    For example:

    <div class="formalpara">

    <div class="title">

    `Subscription` object with proxy setting overrides

    </div>

    ``` yaml
    apiVersion: operators.coreos.com/v1alpha1
    kind: Subscription
    metadata:
      name: etcd-config-test
      namespace: openshift-operators
    spec:
      config:
        env:
        - name: HTTP_PROXY
          value: test_http
        - name: HTTPS_PROXY
          value: test_https
        - name: NO_PROXY
          value: test
      channel: clusterwide-alpha
      installPlanApproval: Automatic
      name: etcd
      source: community-operators
      sourceNamespace: openshift-marketplace
      startingCSV: etcdoperator.v0.9.4-clusterwide
    ```

    </div>

    > [!NOTE]
    > These environment variables can also be unset using an empty value to remove any previously set cluster-wide or custom proxy settings.

    OLM handles these environment variables as a unit; if at least one of them is set, all three are considered overridden and the cluster-wide defaults are not used for the deployments of the subscribed Operator.

4.  Click **Install** to make the Operator available to the selected namespaces.

5.  After the CSV for the Operator appears in the relevant namespace, you can verify that custom proxy environment variables are set in the deployment. For example, using the CLI:

    ``` terminal
    $ oc get deployment -n openshift-operators \
        etcd-operator -o yaml \
        | grep -i "PROXY" -A 2
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
            - name: HTTP_PROXY
              value: test_http
            - name: HTTPS_PROXY
              value: test_https
            - name: NO_PROXY
              value: test
            image: quay.io/coreos/etcd-operator@sha256:66a37fd61a06a43969854ee6d3e21088a98b93838e284a6086b13917f96b0d9c
    ...
    ```

    </div>

</div>

# Injecting a custom CA certificate

When a cluster administrator adds a custom CA certificate to a cluster using a config map, the Cluster Network Operator merges the user-provided certificates and system CA certificates into a single bundle. You can inject this merged bundle into your Operator running on Operator Lifecycle Manager (OLM), which is useful if you have a man-in-the-middle HTTPS proxy.

<div>

<div class="title">

Prerequisites

</div>

- Access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.

- Custom CA certificate added to the cluster using a config map.

- Desired Operator installed and running on OLM.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an empty config map in the namespace where the subscription for your Operator exists and include the following label:

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: trusted-ca
      labels:
        config.openshift.io/inject-trusted-cabundle: "true"
    ```

    - Name of the config map.

    - Requests the Cluster Network Operator to inject the merged bundle.

      After creating this config map, it is immediately populated with the certificate contents of the merged bundle.

2.  Update the `Subscription` object to include a `spec.config` section that mounts the `trusted-ca` config map as a volume to each container within a pod that requires a custom CA:

    ``` yaml
    apiVersion: operators.coreos.com/v1alpha1
    kind: Subscription
    metadata:
      name: my-operator
    spec:
      package: etcd
      channel: alpha
      config:
        selector:
          matchLabels:
            <labels_for_pods>
        volumes:
        - name: trusted-ca
          configMap:
            name: trusted-ca
            items:
              - key: ca-bundle.crt
                path: tls-ca-bundle.pem
        volumeMounts:
        - name: trusted-ca
          mountPath: /etc/pki/ca-trust/extracted/pem
          readOnly: true
    ```

    - Add a `config` section if it does not exist.

    - Specify labels to match pods that are owned by the Operator.

    - Create a `trusted-ca` volume.

    - `ca-bundle.crt` is required as the config map key.

    - `tls-ca-bundle.pem` is required as the config map path.

    - Create a `trusted-ca` volume mount.

      > [!NOTE]
      > Deployments of an Operator can fail to validate the authority and display a `x509 certificate signed by unknown authority` error. This error can occur even after injecting a custom CA when using the subscription of an Operator. In this case, you can set the `mountPath` as `/etc/ssl/certs` for trusted-ca by using the subscription of an Operator.

</div>

# Additional resources

- [Proxy certificates](../../security/certificate_types_descriptions/proxy-certificates.md#proxy-certificates)

- [Replacing the default ingress certificate](../../security/certificates/replacing-default-ingress-certificate.md#replacing-default-ingress)

- [Updating the CA bundle](../../security/certificates/updating-ca-bundle.md#updating-ca-bundle)
