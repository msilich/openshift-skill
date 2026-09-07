<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use Transport Layer Security (TLS) encryption with Red Hat OpenShift GitOps to secure communication between Argo CD components and the Redis cache, protecting sensitive data in transit.

You can secure communication with Redis by using one of the following configurations:

- Enable the `autotls` setting to automatically generate and configure a certificate for TLS encryption.

- Manually configure the TLS encryption by creating the `argocd-operator-redis-tls` secret with a key and certificate pair.

Both configurations are possible with or without High Availability (HA).

# Prerequisites

- You have access to the cluster with `cluster-admin` privileges.

- You have access to the OpenShift Container Platform web console.

- Red Hat OpenShift GitOps Operator is installed on your cluster.

# Configuring TLS for Redis with autotls enabled

You can configure TLS encryption for Redis by enabling the `autotls` setting on a new or already existing Argo CD instance. The configuration automatically provisions the `argocd-operator-redis-tls` secret and does not require further steps. Currently, OpenShift Container Platform is the only supported secret provider.

> [!NOTE]
> By default, the `autotls` setting is disabled.

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  Create an Argo CD instance with `autotls` enabled:

    1.  In the **Administrator** perspective of the web console, use the left navigation panel to go to **Administration** → **CustomResourceDefinitions**.

    2.  Search for `argocds.argoproj.io` and click `ArgoCD` custom resource definition (CRD).

    3.  On the **CustomResourceDefinition details** page, click the **Instances** tab, and then click **Create ArgoCD**.

    4.  Edit or replace the YAML similar to the following example:

        **Example Argo CD CR with autotls enabled:**

        ``` yaml
        apiVersion: argoproj.io/v1beta1
        kind: ArgoCD
        metadata:
          name: argocd
          namespace: openshift-gitops
        spec:
          redis:
            autotls: openshift
          ha:
            enabled: true
        ```

        where:

        `metadata.name`
        Specifies the name of the Argo CD instance.

        `metadata.namespace`
        Specifies the namespace where the Argo CD instance runs.

        `spec.redis.autotls`
        Enables automatic TLS certificate generation for Redis. Set to `openshift` to use the OpenShift service CA.

        `spec.ha.enabled`
        Enables the HA feature. Omit this field or set it to `false` to disable HA.

        > [!TIP]
        > Alternatively, you can enable the `autotls` setting on an already existing Argo CD instance by running the following command:
        >
        > ``` terminal
        > $ oc patch argocds.argoproj.io <instance-name> \
        >   --type=merge \
        >   -p '{"spec":{"redis":{"autotls":"openshift"}}}' \
        >   -n <namespace>
        > ```

    5.  Click **Create**.

    6.  Verify that the Argo CD pods are ready and running:

        ``` terminal
        $ oc get pods -n <namespace>
        ```

        where:

        `<namespace>`
        Specifies a namespace where the Argo CD instance is running, for example `openshift-gitops`.

        **Example output with HA disabled:**

        ``` terminal
        NAME                                  READY   STATUS    RESTARTS   AGE
        argocd-application-controller-0       1/1     Running   0          26s
        argocd-redis-84b77d4f58-vp6zm         1/1     Running   0          37s
        argocd-repo-server-5b959b57f4-znxjq   1/1     Running   0          37s
        argocd-server-6b8787d686-wv9zh        1/1     Running   0          37s
        ```

        > [!NOTE]
        > The HA-enabled TLS configuration requires a cluster with at least three worker nodes. It can take a few minutes for the output to appear if you have enabled the Argo CD instances with HA configuration.

        **Example output with HA enabled:**

        ``` terminal
        NAME                                       READY   STATUS    RESTARTS   AGE
        argocd-application-controller-0            1/1     Running   0          10m
        argocd-redis-ha-haproxy-669757fdb7-5xg8h   1/1     Running   0          10m
        argocd-redis-ha-server-0                   2/2     Running   0          9m9s
        argocd-redis-ha-server-1                   2/2     Running   0          98s
        argocd-redis-ha-server-2                   2/2     Running   0          53s
        argocd-repo-server-576499d46d-8hgbh        1/1     Running   0          10m
        argocd-server-9486f88b7-dk2ks              1/1     Running   0          10m
        ```

3.  Verify that the `argocd-operator-redis-tls` secret is created:

    ``` terminal
    $ oc get secrets argocd-operator-redis-tls -n <namespace>
    ```

    where:

    `<namespace>`
    Specifies the namespace where the Argo CD instance is running, for example `openshift-gitops`.

    **Example output:**

    ``` terminal
    NAME                        TYPE                DATA   AGE
    argocd-operator-redis-tls   kubernetes.io/tls   2      30s
    ```

    The secret must be of type `kubernetes.io/tls` and contain 2 data fields (certificate and key).

</div>

# Configuring TLS for Redis with autotls disabled

You can manually configure TLS encryption for Redis by creating the `argocd-operator-redis-tls` secret with a key and certificate pair and annotating the secret to associate it with the appropriate Argo CD instance.

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  Create an Argo CD instance:

    1.  In the **Administrator** perspective of the web console, go to **Administration** → **CustomResourceDefinitions**.

    2.  Search for `argocds.argoproj.io` and click `ArgoCD`.

    3.  On the **CustomResourceDefinition details** page, click the **Instances** tab, and then click **Create ArgoCD**.

    4.  Edit or replace the YAML similar to the following example:

        ``` yaml
        apiVersion: argoproj.io/v1beta1
        kind: ArgoCD
        metadata:
          name: argocd
          namespace: openshift-gitops
        spec:
          ha:
            enabled: true
        ```

        where:

        `metadata.name`
        Specifies the name of the Argo CD instance.

        `metadata.namespace`
        Specifies the namespace where you want to run the Argo CD instance.

        `spec.ha.enabled`
        Specifies the flag value that enables the HA feature. If you do not want to enable HA, do not include this line or set the flag value as `false`.

    5.  Click **Create**.

    6.  Verify that the Argo CD pods are ready and running:

        ``` terminal
        $ oc get pods -n <namespace>
        ```

        where:

        `<namespace>`
        Specifies a namespace where the Argo CD instance is running, for example `openshift-gitops`.

        **Example output with HA disabled:**

        ``` terminal
        NAME                                  READY   STATUS    RESTARTS   AGE
        argocd-application-controller-0       1/1     Running   0          26s
        argocd-redis-84b77d4f58-vp6zm         1/1     Running   0          37s
        argocd-repo-server-5b959b57f4-znxjq   1/1     Running   0          37s
        argocd-server-6b8787d686-wv9zh        1/1     Running   0          37s
        ```

        > [!NOTE]
        > The HA-enabled TLS configuration requires a cluster with at least three worker nodes. It can take a few minutes for the output to appear if you have enabled the Argo CD instances with HA configuration.

        **Example output with HA enabled:**

        ``` terminal
        NAME                                       READY   STATUS    RESTARTS   AGE
        argocd-application-controller-0            1/1     Running   0          10m
        argocd-redis-ha-haproxy-669757fdb7-5xg8h   1/1     Running   0          10m
        argocd-redis-ha-server-0                   2/2     Running   0          9m9s
        argocd-redis-ha-server-1                   2/2     Running   0          98s
        argocd-redis-ha-server-2                   2/2     Running   0          53s
        argocd-repo-server-576499d46d-8hgbh        1/1     Running   0          10m
        argocd-server-9486f88b7-dk2ks              1/1     Running   0          10m
        ```

3.  Create a self-signed certificate for the Redis server:

    - For the Argo CD instance with HA disabled:

      ``` terminal
      $ openssl req -new -x509 -sha256 \
        -subj "/C=XX/ST=XX/O=Testing/CN=redis" \
        -reqexts SAN -extensions SAN \
        -config <(printf "\n[SAN]\nsubjectAltName=DNS:argocd-redis.<namespace>.svc.cluster.local\n[req]\ndistinguished_name=req") \
        -keyout /tmp/redis.key \
        -out /tmp/redis.crt \
        -newkey rsa:4096 \
        -nodes \
        -days 10
      ```

      where:

      `<namespace>`
      Specifies a namespace where the Argo CD instance is running, for example `openshift-gitops`.

      **Example output:**

      ``` terminal
      Generating a RSA private key
      ...............++++
      ............................++++
      writing new private key to '/tmp/redis.key'
      ```

    - For the Argo CD instance with HA enabled:

      ``` terminal
      $ openssl req -new -x509 -sha256 \
        -subj "/C=XX/ST=XX/O=Testing/CN=redis" \
        -reqexts SAN -extensions SAN \
        -config <(printf "\n[SAN]\nsubjectAltName=DNS:argocd-redis-ha-haproxy.<namespace>.svc.cluster.local\n[req]\ndistinguished_name=req") \
        -keyout /tmp/redis-ha.key \
        -out /tmp/redis-ha.crt \
        -newkey rsa:4096 \
        -nodes \
        -days 10
      ```

      where:

      `<namespace>`
      Specifies a namespace where the Argo CD instance is running, for example `openshift-gitops`.

      **Example output:**

      ``` terminal
      Generating a RSA private key
      ...............++++
      ............................++++
      writing new private key to '/tmp/redis-ha.key'
      ```

4.  Verify that the generated files are available:

    ``` terminal
    $ cd /tmp
    $ ls
    ```

    **Example output with HA disabled:**

    ``` terminal
    ...
    redis.crt
    redis.key
    ...
    ```

    **Example output with HA enabled:**

    ``` terminal
    ...
    redis-ha.crt
    redis-ha.key
    ...
    ```

5.  Create the `argocd-operator-redis-tls` secret:

    - For the Argo CD instance with HA disabled:

      ``` terminal
      $ oc create secret tls argocd-operator-redis-tls \
        --key=/tmp/redis.key \
        --cert=/tmp/redis.crt \
        -n <namespace>
      ```

      where:

      `<namespace>`
      Specifies the namespace where the Argo CD instance is running, for example `openshift-gitops`.

    - For the Argo CD instance with HA enabled:

      ``` terminal
      $ oc create secret tls argocd-operator-redis-tls \
        --key=/tmp/redis-ha.key \
        --cert=/tmp/redis-ha.crt \
        -n <namespace>
      ```

      where:

      `<namespace>`
      Specifies the namespace where the Argo CD instance is running, for example `openshift-gitops`.

      **Example output:**

      ``` terminal
      secret/argocd-operator-redis-tls created
      ```

6.  Annotate the secret to indicate that it belongs to the Argo CD CR:

    ``` terminal
    $ oc annotate secret argocd-operator-redis-tls \
      argocds.argoproj.io/name=<instance-name> \
      -n <namespace>
    ```

    where:

    `<instance-name>`
    Specifies a name of the Argo CD instance, for example `argocd`.

    `<namespace>`
    Specifies the namespace where the Argo CD instance is running, for example `openshift-gitops`.

    **Example output:**

    ``` terminal
    secret/argocd-operator-redis-tls annotated
    ```

7.  Verify that the Argo CD pods are ready and running:

    ``` terminal
    $ oc get pods -n <namespace>
    ```

    where:

    `<namespace>`
    Specifies a namespace where the Argo CD instance is running, for example `openshift-gitops`.

    **Example output with HA disabled:**

    ``` terminal
    NAME                                  READY   STATUS    RESTARTS   AGE
    argocd-application-controller-0       1/1     Running   0          26s
    argocd-redis-84b77d4f58-vp6zm         1/1     Running   0          37s
    argocd-repo-server-5b959b57f4-znxjq   1/1     Running   0          37s
    argocd-server-6b8787d686-wv9zh        1/1     Running   0          37s
    ```

    > [!NOTE]
    > It can take a few minutes for the output to appear if you have enabled the Argo CD instances with HA configuration.

    **Example output with HA enabled:**

    ``` terminal
    NAME                                       READY   STATUS    RESTARTS   AGE
    argocd-application-controller-0            1/1     Running   0          10m
    argocd-redis-ha-haproxy-669757fdb7-5xg8h   1/1     Running   0          10m
    argocd-redis-ha-server-0                   2/2     Running   0          9m9s
    argocd-redis-ha-server-1                   2/2     Running   0          98s
    argocd-redis-ha-server-2                   2/2     Running   0          53s
    argocd-repo-server-576499d46d-8hgbh        1/1     Running   0          10m
    argocd-server-9486f88b7-dk2ks              1/1     Running   0          10m
    ```

</div>
