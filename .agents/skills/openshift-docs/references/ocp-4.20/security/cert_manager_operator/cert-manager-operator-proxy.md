<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

If a cluster-wide egress proxy is configured in OpenShift Container Platform, Operator Lifecycle Manager (OLM) automatically configures Operators that it manages with the cluster-wide proxy. OLM automatically updates all of the Operator’s deployments with the `HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY` environment variables.

You can inject any CA certificates that are required for proxying HTTPS connections into the cert-manager Operator for Red Hat OpenShift.

# Injecting a custom CA certificate for the cert-manager Operator for Red Hat OpenShift

If your OpenShift Container Platform cluster has the cluster-wide proxy enabled, you can inject any CA certificates that are required for proxying HTTPS connections into the cert-manager Operator for Red Hat OpenShift.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have enabled the cluster-wide proxy for OpenShift Container Platform.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a config map in the `cert-manager` namespace by running the following command:

    ``` terminal
    $ oc create configmap trusted-ca -n cert-manager
    ```

2.  Inject the CA bundle that is trusted by OpenShift Container Platform into the config map by running the following command:

    ``` terminal
    $ oc label cm trusted-ca config.openshift.io/inject-trusted-cabundle=true -n cert-manager
    ```

3.  Update the deployment for the cert-manager Operator for Red Hat OpenShift to use the config map by running the following command:

    ``` terminal
    $ oc -n cert-manager-operator patch subscription openshift-cert-manager-operator --type='merge' -p '{"spec":{"config":{"env":[{"name":"TRUSTED_CA_CONFIGMAP_NAME","value":"trusted-ca"}]}}}'
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the deployments have finished rolling out by running the following command:

    ``` terminal
    $ oc rollout status deployment/cert-manager-operator-controller-manager -n cert-manager-operator && \
    oc rollout status deployment/cert-manager -n cert-manager && \
    oc rollout status deployment/cert-manager-webhook -n cert-manager && \
    oc rollout status deployment/cert-manager-cainjector -n cert-manager
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    deployment "cert-manager-operator-controller-manager" successfully rolled out
    deployment "cert-manager" successfully rolled out
    deployment "cert-manager-webhook" successfully rolled out
    deployment "cert-manager-cainjector" successfully rolled out
    ```

    </div>

2.  Verify that the CA bundle was mounted as a volume by running the following command:

    ``` terminal
    $ oc get deployment cert-manager -n cert-manager -o=jsonpath={.spec.template.spec.'containers[0].volumeMounts'}
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    [{"mountPath":"/etc/pki/tls/certs/cert-manager-tls-ca-bundle.crt","name":"trusted-ca","subPath":"ca-bundle.crt"}]
    ```

    </div>

3.  Verify that the source of the CA bundle is the `trusted-ca` config map by running the following command:

    ``` terminal
    $ oc get deployment cert-manager -n cert-manager -o=jsonpath={.spec.template.spec.volumes}
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    [{"configMap":{"defaultMode":420,"name":"trusted-ca"},"name":"trusted-ca"}]
    ```

    </div>

</div>

# Additional resources

- [Configuring proxy support in Operator Lifecycle Manager](../../operators/admin/olm-configuring-proxy-support.md#olm-configuring-proxy-support)
