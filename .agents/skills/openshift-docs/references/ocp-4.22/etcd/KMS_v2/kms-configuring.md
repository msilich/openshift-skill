<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can configure external KMS encryption for etcd to centralize key management and meet regulatory compliance requirements.

> [!IMPORTANT]
> Kubernetes KMS v2 is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

# Enable KMS encryption

You can enable external Key Management Service (KMS) encryption for etcd data to centralize key management and meet compliance requirements.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have enabled the `TechPreviewNoUpgrade` feature set to enable the `KMSEncryption` feature gate.

- You have a `HashiCorp Vault Enterprise` instance accessible from your control plane nodes. Vault Community Edition is not available.

- Your control plane nodes have network access to the Vault server.

- You have configured your Vault instance with:

  - Transit secrets engine enabled at the default `transit/` mount path

  - Encryption key created with type `aes256-gcm96` (recommended for FIPS 140-3 compliance)

  - Vault policy allowing the Kubernetes KMS v2 plugin to encrypt, decrypt, and read key information

  - Authentication method (token, `AppRole`, or `userpass`) configured with the policy attached

</div>

The Kubernetes KMS v2 plugin requires a Vault policy with the following capabilities:

``` hcl
path "transit/encrypt/kms-key" {
  capabilities = ["update"]
}

path "transit/decrypt/kms-key" {
  capabilities = ["update"]
}

path "transit/keys/kms-key" {
  capabilities = ["read"]
}

path "auth/token/lookup-self" {
  capabilities = ["read"]
}
```

Replace `kms-key` with your Vault Transit key name if using a different name.

> [!IMPORTANT]
> Create an etcd backup before enabling KMS encryption.

<div>

<div class="title">

Procedure

</div>

1.  Deploy the KMS plugin on each control plane host as a static pod:

    - Configure the plugin to listen at `unix:///var/run/kmsplugin/kms.sock`

    - For your static pod, mount `/var/run/kmsplugin` as `hostPath`

    - Configure KMS provider connection details and authentication credentials

    The following steps show how to deploy the `HashiCorp` Vault KMS plugin as a static pod.

2.  Create a static pod manifest file:

    ``` terminal
    $ cat > /tmp/vault-kms-plugin.yaml <<'EOF'
    apiVersion: v1
    kind: Pod
    metadata:
      name: vault-kms-plugin
      namespace: kube-system
      labels:
        app: vault-kms-plugin
        tier: control-plane
    spec:
      priorityClassName: system-node-critical
      hostNetwork: true
      containers:
      - name: vault-kms-plugin
        image: quay.io/redhat-isv-containers/698df066f8d1ddf179c15ef9:<version>
        command:
        - /vault-kubernetes-kms
        - -vault-address=<https://vault.example.com:8200>
        - -<vault_namespace>=admin
        - -auth-method=userpass
        - -userpass-username=<vault_username>
        - -userpass-password=<vault_password>
        - -transit-mount=transit
        - -transit-key=kms-key
        - -socket=unix:///var/run/kmsplugin/kms.sock
        volumeMounts:
        - name: kmsplugin
          mountPath: /var/run/kmsplugin
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 512Mi
        securityContext:
          privileged: true
      volumes:
      - name: kmsplugin
        hostPath:
          path: /var/run/kmsplugin
          type: DirectoryOrCreate
    EOF
    ```

    Replace the following values to match your environment:

    \<version\>
    The Vault KMS plugin image version tag. Use `0.1.0-beta-ubi`.

    \<vault_username\>
    Your Vault username for authentication.

    \<vault_password\>
    Your Vault password for authentication.

    <https://vault.example.com:8200>
    The Vault address. Update this field to match your Vault server URL.

    \<vault_namespace\>
    Optional field.

    The manifest uses the Red Hat certified container image from Quay.io (`quay.io/redhat-isv-containers/698df066f8d1ddf179c15ef9`), which is the recommended image for OpenShift Container Platform.

    > [!NOTE]
    > Alternatively, you can use the [HashiCorp image from Docker Hub](https://hub.docker.com/r/hashicorp/vault-kube-kms) by replacing the image field with `docker.io/hashicorp/vault-kube-kms:0.1.0-beta-ubi`.

3.  Deploy the static pod manifest to each control plane node by running the following commands:

    ``` terminal
    $ MANIFEST=$(cat /tmp/vault-kms-plugin.yaml | base64)
    $ for node in $(oc get nodes --selector=node-role.kubernetes.io/master -o name | cut -d/ -f2); do
        echo "Deploying to $node..."
        oc debug node/$node -- chroot /host bash -c \
          "echo '$MANIFEST' | base64 -d > /etc/kubernetes/manifests/vault-kms-plugin.yaml"
      done
    ```

    The kubelet automatically detects and starts static pods from `/etc/kubernetes/manifests/`.

4.  Verify the static pods are running by entering the following command:

    ``` terminal
    $ oc get pods -n kube-system -o wide | grep vault-kms
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    vault-kms-plugin-ip-10-0-16-7.compute.internal    1/1  Running  0  2m  10.0.16.7
    vault-kms-plugin-ip-10-0-32-93.compute.internal   1/1  Running  0  2m  10.0.32.93
    vault-kms-plugin-ip-10-0-69-106.compute.internal  1/1  Running  0  2m  10.0.69.106
    ```

    </div>

    Static pod names include the node name as a suffix. You should see one pod per control plane node.

5.  Verify the socket exists on a control plane node by entering the following command:

    ``` terminal
    $ oc debug node/<node_name> -- chroot /host ls -la /var/run/kmsplugin/kms.sock
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    srwxr-xr-x. 1 root root 0 <timestamp> /var/run/kmsplugin/kms.sock
    ```

    </div>

    > [!NOTE]
    > Static pods are managed by kubelet on each node and cannot be deleted with `oc delete pod`. To remove a static pod, delete the manifest file from `/etc/kubernetes/manifests/` on each control plane node.

6.  Edit the `APIServer` custom resource by entering the following command:

    ``` terminal
    $ oc edit apiserver cluster
    ```

7.  Add the KMS configuration to the `spec.encryption` section:

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: APIServer
    metadata:
      name: cluster
    spec:
      encryption:
        type: KMS
    ```

8.  Save and exit.

    Migration begins automatically. The `kube-apiserver`, `openshift-apiserver` and `oauth-apiserver` Operators will restart and roll out new revisions.

    > [!NOTE]
    > The `openshift-apiserver` and `authentication` operators typically complete migration in 5-10 minutes. The `kube-apiserver` operator uses a conservative rollout strategy, updating one control plane node at a time and waiting for health checks before proceeding to the next node. This process can take 30 minutes or longer depending on cluster load.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify the encryption type by entering the following command:

    ``` terminal
    $ oc get apiserver cluster -o jsonpath='{.spec.encryption.type}'
    ```

    Output should show `KMS`.

2.  Monitor the `kube-apiserver` rollout progress by entering the following command:

    ``` terminal
    $ oc get kubeapiserver cluster -o jsonpath='{.status.nodeStatuses}' | jq -r '.[] | "\(.nodeName | split(".")[0]): current=\(.currentRevision) target=\(.targetRevision)"'
    ```

    <div class="formalpara">

    <div class="title">

    Example output during rollout

    </div>

    ``` terminal
    ip-10-0-16-166: current=10 target=0
    ip-10-0-32-93: current=9 target=10
    ip-10-0-69-106: current=9 target=0
    ```

    </div>

    The operator rolls out one node at a time. When all nodes show the same `current` revision and `target` is `0`, the rollout is complete.

3.  Check the encryption migration status by entering the following command:

    ``` terminal
    $ oc get kubeapiserver cluster -o jsonpath='{.status.conditions[?(@.type=="Encrypted")]}' | jq .
    ```

    <div class="formalpara">

    <div class="title">

    Example output when complete

    </div>

    ``` terminal
    {
      "lastTransitionTime": "2026-05-15T17:39:02Z",
      "message": "All resources encrypted: secrets, configmaps",
      "reason": "EncryptionCompleted",
      "status": "True",
      "type": "Encrypted"
    }
    ```

    </div>

    Wait for `reason` to show `EncryptionCompleted` before proceeding to verify encryption in etcd.

4.  Verify secrets are encrypted in etcd:

    > [!WARNING]
    > Wait for the `kube-apiserver` rollout to complete on all control plane nodes before verifying encryption. During the rollout, API requests are distributed across nodes, and secrets created while some nodes are still on an earlier revision will not be encrypted with Kubernetes KMS v2.

    1.  Create a test secret by entering the following command:

        ``` terminal
        $ oc create secret generic test-secret --from-literal=key=value -n default
        ```

    2.  Get an etcd pod name by entering the following command:

        ``` terminal
        $ oc get pods -n openshift-etcd -l app=etcd -o name | head -1
        ```

    3.  Check the secret data in etcd by entering the following command:

        ``` terminal
        $ oc exec -n openshift-etcd <etcd_pod_name> -- etcdctl get /kubernetes.io/secrets/default/test-secret --print-value-only | hexdump -C | head -1
        ```

        Output should begin with `k8s:enc:kms:v2:` followed by encrypted binary data.

    4.  Delete the test secret by entering the following command:

        ``` terminal
        $ oc delete secret test-secret -n default
        ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Vault Transit Secrets Engine](https://developer.hashicorp.com/vault/docs/secrets/transit)

- [Vault API: Create Key](https://developer.hashicorp.com/vault/api-docs/secret/transit#create-key)

- [Vault Policies](https://developer.hashicorp.com/vault/docs/concepts/policies)

- [Vault Authentication Methods](https://developer.hashicorp.com/vault/docs/auth)

</div>

# Rotate the Vault encryption key

You can rotate your Vault Transit encryption key to generate a new key version while maintaining access to data encrypted with earlier versions.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have access to your Vault instance with permissions to rotate keys.

- Kubernetes KMS v2 encryption is enabled and functioning.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Rotate the Vault encryption key by entering the following command:

    ``` terminal
    $ vault write -f transit/keys/kms-key/rotate
    ```

    Vault creates a new key version while maintaining earlier versions for decryption. The API server automatically uses the correct key version for each secret.

2.  Verify the new key version by entering the following command:

    ``` terminal
    $ vault read transit/keys/kms-key
    ```

    The `latest_version` field shows the current key version number.

</div>

<div>

<div class="title">

Verification

</div>

- Verify that existing secrets remain accessible by entering the following command:

  ``` terminal
  $ oc get secret -A
  ```

</div>

All secrets should be readable without errors.

> [!NOTE]
> Existing encrypted secrets do not need re-encryption. Vault maintains all key versions and automatically uses the appropriate version for decryption.

<div>

<div class="title">

Additional resources

</div>

- [Vault Transit: Rotate Key](https://developer.hashicorp.com/vault/api-docs/secret/transit#rotate-key)

- [Vault Transit: Rewrap Data](https://developer.hashicorp.com/vault/api-docs/secret/transit#rewrap-data)

- [Vault Transit: Key Rotation](https://developer.hashicorp.com/vault/docs/secrets/transit#key-rotation)

</div>

# Migrate from local encryption to KMS encryption

You can migrate from local etcd encryption to external KMS encryption to centralize key management and improve compliance.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have enabled the `TechPreviewNoUpgrade` feature set to enable the `KMSEncryption` feature gate.

- Your cluster is currently using `aescbc` or `aesgcm` encryption.

- You have deployed the KMS plugin on all control plane nodes.

- Control plane nodes have network access to the KMS provider.

</div>

> [!IMPORTANT]
> Create an etcd backup before migrating.

<div>

<div class="title">

Procedure

</div>

1.  Back up the current etcd encryption configuration by entering the following command:

    ``` terminal
    $ oc get apiserver cluster -o yaml > apiserver-backup.yaml
    ```

2.  Edit the APIServer custom resource by entering the following command:

    ``` terminal
    $ oc edit apiserver cluster
    ```

3.  Change the encryption type from `aescbc` or `aesgcm` to `KMS`:

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: APIServer
    metadata:
      name: cluster
    spec:
      encryption:
        type: KMS
    ```

4.  Save and exit.

    Migration starts automatically and typically takes several minutes.

5.  Verify migration completion for all API servers by running the following commands:

    ``` terminal
    $ oc get openshiftapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{"\n"}{end}'
    ```

    ``` terminal
    $ oc get kubeapiserver -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{"\n"}{end}'
    ```

    ``` terminal
    $ oc get authentication.operator.openshift.io -o=jsonpath='{range .items[0].status.conditions[?(@.type=="Encrypted")]}{"\n"}{end}'
    ```

    All outputs should show `EncryptionCompleted`.

</div>

# Monitor KMS encryption status

You can monitor KMS encryption status by using Operator and API server logs to verify successful configuration and detect issues.

<div>

<div class="title">

Procedure

</div>

1.  Check the kube-apiserver operator logs for KMS-related events by entering the following command:

    ``` terminal
    $ oc logs -n openshift-kube-apiserver-operator deploy/kube-apiserver-operator | grep -i kms
    ```

2.  View API server logs for KMS-related events by entering the following command:

    ``` terminal
    $ oc logs -n openshift-kube-apiserver -l apiserver=true --tail=100 | grep -i kms
    ```

3.  Verify the KMS encryption configuration by entering the following command:

    ``` terminal
    $ oc get apiserver cluster -o jsonpath='{.spec.encryption}' | jq
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Kubernetes KMS provider documentation](https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/)

</div>

# KMS encryption troubleshooting

You can diagnose and resolve common KMS encryption issues to maintain secure key management and cluster availability.

## Invalid KMS configuration

**Symptom:** APIServer resource shows validation errors during KMS encryption configuration.

**Diagnosis:** Check kube-apiserver Operator logs:

``` terminal
$ oc logs -n openshift-kube-apiserver-operator deploy/kube-apiserver-operator | grep -i "kms\|validation\|error"
```

**Solutions:**

- Verify plugin configuration follows provider requirements

- Ensure all required fields are specified

- Verify plugin is running on all control plane nodes:

  ``` terminal
  $ oc debug node/<node_name> -- chroot /host ls -la /var/run/kmsplugin/kms.sock
  ```

## KMS permissions errors

**Symptom:** Encryption migration fails with permission errors.

**Diagnosis:** Check Operator and plugin logs:

``` terminal
$ oc logs -n openshift-kube-apiserver-operator deploy/kube-apiserver-operator | grep -i "kms\|permission\|access denied"
```

``` terminal
$ oc debug node/<node_name> -- chroot /host journalctl -u kms-plugin
```

**Solutions:**

- Verify plugin has valid authentication credentials

- Check if credentials have expired

- Ensure plugin principal has encrypt and decrypt permissions

- Verify KMS provider key policy allows plugin access

- Confirm encryption key is enabled and not scheduled for deletion

## Expired or deleted KMS key

**Symptom:** API server cannot decrypt secrets when accessing encrypted resources.

**Diagnosis:** Check logs and verify key status:

``` terminal
$ oc logs -n openshift-kube-apiserver -l apiserver=true | grep -i "decrypt\|kms.*error"
```

``` terminal
$ oc debug node/<node_name> -- chroot /host journalctl -u kms-plugin | grep -i "key\|error"
```

**Solutions:**

- Re-enable the encryption key if disabled

- Restore from backup if key was permanently deleted

- Cancel key deletion if scheduled

- Ensure KMS provider maintains access to previous key versions

> [!WARNING]
> Deleted KMS keys prevent data recovery. Align key retention with backup policies.

## API server degraded or unavailable

**Symptom:** API server becomes degraded or unresponsive after enabling KMS encryption.

**Diagnosis:** Check Operator status and logs:

``` terminal
$ oc get clusteroperator kube-apiserver
```

``` terminal
$ oc logs -n openshift-kube-apiserver -l apiserver=true --tail=200 | grep -i kms
```

**Solutions:**

- Check network connectivity between control plane and KMS provider

- Verify network policies, firewalls, and routes allow communication

- Monitor KMS provider rate limits and request increases if needed

- Verify DNS resolution and TLS certificate validation

- Confirm plugin is running on all control plane nodes:

  ``` terminal
  $ oc debug node/<node_name> -- chroot /host systemctl status kms-plugin
  ```

## Encryption migration stuck or slow

**Symptom:** KMS encryption migration takes unusually long or becomes stuck.

**Diagnosis:** Check Operator status and migration logs:

``` terminal
$ oc get clusteroperator kube-apiserver
```

``` terminal
$ oc logs -n openshift-kube-apiserver-operator deploy/kube-apiserver-operator | grep -i migration
```

**Solutions:**

- Migration time depends on data size; monitor progress

- Monitor KMS provider audit logs for rate limiting or throttling events

- Check network performance between control plane and KMS provider

## Collecting debug information

Collect cluster logs:

``` terminal
$ oc adm must-gather
```

``` terminal
$ oc get apiserver cluster -o yaml > apiserver.yaml
```

``` terminal
$ oc logs -n openshift-kube-apiserver-operator deploy/kube-apiserver-operator > kube-apiserver-operator.log
```

``` terminal
$ oc logs -n openshift-kube-apiserver -l apiserver=true --tail=500 > kube-apiserver.log
```

Collect KMS provider information:

- KMS plugin logs from control plane nodes

- KMS provider audit logs

- KMS provider key policy and permissions

- Authentication credentials status

- Network connectivity test results

> [!NOTE]
> Redact credentials, tokens, and sensitive data before sharing logs.

# Additional resources

- [Using a KMS provider for data encryption](https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/)

- [HashiCorp Vault Transit Secrets Engine](https://developer.hashicorp.com/vault/docs/secrets/transit)

- [Use Vault as a Kubernetes KMS provider](https://developer.hashicorp.com/vault/docs/deploy/kubernetes/kms)

- [HashiCorp Vault KMS plugin container image](https://hub.docker.com/r/hashicorp/vault-kube-kms)
