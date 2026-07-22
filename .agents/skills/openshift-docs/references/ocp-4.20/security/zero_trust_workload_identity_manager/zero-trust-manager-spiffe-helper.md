<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

SPIFFE Helper writes Transport Layer Security (TLS) certificates to disk for applications that cannot use the SPIFFE Workload API. Use it to eliminate manual certificate management and reduce the risk of expired certificates.

# SPIFFE Helper container image

Use SPIFFE Helper with the Zero Trust Workload Identity Manager when your application cannot call the workload API directly but can read TLS certificates from a shared volume.

SPIFFE Helper is a utility that connects to the SPIFFE Workload API, fetches identity credentials, writes them to files on disk, and optionally notifies a workload when X.509 material is renewed.

The Zero Trust Workload Identity Manager provides a supported SPIFFE Helper container image based on the upstream SPIFFE Helper. The configuration file format, command-line flags, and workload API behavior are compatible with upstream.

SPIFFE Helper performs the following tasks:

1.  Connects to the SPIFFE Workload API, usually through the SPIFFE Runtime Environment Agent socket exposed by the SPIFFE CSI driver.

2.  Fetches X.509 SPIFFE Verifiable Identity Document (SVID)s, JSON Web Token (JWT) SVIDs, and JWT bundles from SPIFFE Runtime Environment.

3.  Writes credentials to files under a configured directory such as `cert_dir`.

4.  Optionally notifies a workload when X.509 authentication credentials are renewed in daemon mode.

# SPIFFE Helper modes

SPIFFE Helper fetches credentials from the SPIFFE Workload API and writes them to disk for workloads that cannot call the API directly. On OpenShift Container Platform, a pod typically uses non-daemon mode in an init container for initial certificates and daemon mode in a sidecar to rotate them before expiring.

SPIFFE Helper runs in one of two modes:

- **Non-daemon mode** (`-daemon-mode=false` or `daemon_mode = false`): Fetches credentials once, writes files, and exits. Use this mode in an init container to bootstrap TLS before the main application starts. In this mode, `cmd` and `renew_signal` are ignored.

- **Daemon mode** (default): Stays running until the pod is terminated or an unrecoverable error occurs. Watches the Workload API and renews credentials before they expire. Supports `cmd`, `pid_file_name`, `renew_signal`, and optional HTTP health checks. SPIFFE Helper does not background itself like a traditional Unix daemon.

On OpenShift Container Platform, a typical pod uses both modes:

- An init container runs SPIFFE Helper in non-daemon mode to populate a shared `emptyDir` volume with initial TLS material.

- A sidecar container runs SPIFFE Helper in daemon mode to rotate certificates before they expire.

- The main application container mounts the shared certificate directory and uses the files for TLS.

The SPIFFE workload API is exposed through the SPIFFE container storage interface (CSI), which mounts the Workload API socket into the pod at a path such as `/spiffe-workload-api/spire-agent.sock`.

The following deployment excerpt shows the init container and sidecar pattern on OpenShift Container Platform:

``` yaml
initContainers:
- name: spiffe-helper-init
  image: registry.redhat.io/zero-trust-workload-identity-manager/spiffe-helper-rhel9:<version>
  args:
  - '-config'
  - /etc/spiffe-helper/helper.conf
  - '-daemon-mode=false'
  volumeMounts:
  - name: spiffe-workload-api
    readOnly: true
    mountPath: /spiffe-workload-api
  - name: postgresql-certs
    mountPath: /opt/postgresql-certs
  - name: spiffe-helper
    mountPath: /etc/spiffe-helper
containers:
- name: spiffe-helper
  image: registry.redhat.io/zero-trust-workload-identity-manager/spiffe-helper-rhel9:<version>
  args:
  - '-config'
  - /etc/spiffe-helper/helper.conf
  volumeMounts:
  - name: spiffe-workload-api
    readOnly: true
    mountPath: /spiffe-workload-api
  - name: postgresql-certs
    mountPath: /opt/postgresql-certs
  - name: spiffe-helper
    mountPath: /etc/spiffe-helper
volumes:
- name: spiffe-workload-api
  csi:
    driver: csi.spiffe.io
    readOnly: true
- name: postgresql-certs
  emptyDir:
    medium: Memory
- name: spiffe-helper
  configMap:
    name: spiffe-helper
```

Replace `<version>` with the tag that matches your Zero Trust Workload Identity Manager installation.

# SPIFFE Helper credential types

SPIFFE Helper supports X.509 SPIFFE Verifiable Identity Document (SVID), JSON Web Token (JWT) bundle, and JWT SVID outputs configured in the SPIFFE Helper configuration file and written under `cert_dir` for workloads that cannot use the workload API directly.

At least one complete set must be specified:

- **X.509 SVID** — Requires `svid_file_name`, `svid_key_file_name`, and `svid_bundle_file_name`. SPIFFE Helper writes Privacy-Enhanced Mail (PEM) certificate, PEM private key, and PEM trust bundle files under `cert_dir`.

- **JWT bundle** — Requires `jwt_bundle_file_name`. SPIFFE Helper writes a JSON bundle file.

- **JWT SVIDs** — Requires one or more `jwt_svids` blocks with `jwt_audience`, `jwt_svid_file_name`, and related settings. SPIFFE Helper writes base64-encoded token files.

The `cert_dir` directory must exist before SPIFFE Helper starts.

The following `helper.conf` excerpt configures X.509 SVID output for a PostgreSQL server:

``` terminal
agent_address = "/spiffe-workload-api/spire-agent.sock"
cert_dir = "/opt/postgresql-certs"
svid_file_name = "svid.pem"
svid_key_file_name = "svid.key"
svid_bundle_file_name = "svid_bundle.pem"
```

The following `helper.conf` excerpt configures JWT SVID output:

``` terminal
agent_address = "/spiffe-workload-api/spire-agent.sock"
cert_dir = "/opt/jwt-certs"
jwt_svids = [{
  jwt_audience = "your-audience"
  jwt_svid_file_name = "jwt_svid.token"
}]
```

For JWT bundle output, set `jwt_bundle_file_name` instead of the X.509 or JWT SVID file names.

# Deploying PostgreSQL with SPIFFE Helper

Deploy a PostgreSQL server and client that use SPIFFE Helper to fetch X.509 SPIFFE Verifiable Identity Document (SVID) from the SPIFFE Workload API and write them to disk for mutual Transport Layer Security (mTLS).

The manifests in this procedure use the Zero Trust Workload Identity Manager SPIFFE Helper image.

When certificates renew, the server must reload PostgreSQL TLS configuration. Containers in the same pod use separate process namespaces, so the SPIFFE Helper sidecar cannot signal the PostgreSQL container directly. Instead, SPIFFE Helper uses the **managed-child** pattern. This pattern in daemon mode it runs `cmd` (`/usr/bin/psql`) with `cmd_args` to execute `SELECT pg_reload_conf();` as a child process inside the helper container whenever X.509 material is updated.

The stock SPIFFE Helper image does not include the `psql` client required for that reload command. Build a custom image that extends the Zero Trust Workload Identity Manager image and adds the PostgreSQL client package.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have installed the Zero Trust Workload Identity Manager.

- The `ZeroTrustWorkloadIdentityManager` custom resource reports `Ready`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `Containerfile` with the following contents:

    ``` dockerfile
    FROM registry.redhat.io/zero-trust-workload-identity-manager/spiffe-helper-rhel9:<version>

    USER 0

    RUN dnf install -y postgresql && \
        dnf clean all

    USER 65534
    ```

    Replace `<version>` with the tag that matches your Zero Trust Workload Identity Manager installation.

2.  Build and push a custom SPIFFE Helper image for the PostgreSQL server by running the following command.

    ``` terminal
    $ podman build -f Containerfile \
      -t <registry>/spiffe-helper-postgresql:latest .
    ```

    ``` terminal
    $ podman push <registry>/spiffe-helper-postgresql:latest
    ```

    Replace `<registry>` with your container registry.

3.  Create the PostgreSQL server resources by using the following example:

    ``` yaml
    $ oc apply -f - << 'EOF'
    ---
    kind: Namespace
    apiVersion: v1
    metadata:
      name: postgresql-spiffe
    ---
    kind: ServiceAccount
    apiVersion: v1
    metadata:
      name: postgresql-spiffe
      namespace: postgresql-spiffe
    ---
    apiVersion: spire.spiffe.io/v1alpha1
    kind: ClusterSPIFFEID
    metadata:
      name: postgresql-spiffe
    spec:
      className: zero-trust-workload-identity-manager-spire
      dnsNameTemplates:
        - postgresql-spiffe.postgresql-spiffe.svc
      namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: postgresql-spiffe
      podSelector:
        matchLabels:
          app: postgresql-spiffe
      spiffeIDTemplate: 'spiffe://{{ .TrustDomain }}/ns/{{ .PodMeta.Namespace }}/sa/{{ .PodSpec.ServiceAccountName }}'
    ---
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: postgres-config
      namespace: postgresql-spiffe
    data:
      pg_hba.conf: |
        # TYPE      DATABASE        USER            ADDRESS                 METHOD
        local       all             all                                     trust
        host        postgres        postgres        127.0.0.1/32            trust
        hostnossl   postgres        postgres        127.0.0.1/32            trust
        hostnossl   all             all             0.0.0.0/0               reject
        hostssl     all             all             0.0.0.0/0               cert
      postgresql.conf: |
        listen_addresses '*'
        ssl = on
        ssl_cert_file = '/opt/postgresql-certs/svid.pem'
        ssl_key_file = '/opt/postgresql-certs/svid.key'
        ssl_ca_file = '/opt/postgresql-certs/svid_bundle.pem'
    ---
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: postgresql-init-db
      namespace: postgresql-spiffe
    data:
      initdb.sh: |
        # Copy configuration files
        cp /opt/pg_hba/pg_hba.conf /var/lib/pgsql/data/userdata
        # Create postgresql resources
        psql -U postgres <<!!EOF
            CREATE DATABASE $SPIFFE_DATABASE;
            CREATE USER $SPIFFE_USER WITH encrypted password '$SPIFFE_PASSWORD';
            GRANT ALL privileges ON database $SPIFFE_DATABASE TO $SPIFFE_USER;
            \c $SPIFFE_DATABASE;
            CREATE TABLE test_table (
              id bigserial primary key,
              name VARCHAR(255) NOT NULL,
              text VARCHAR(255) NOT NULL
            );
            GRANT ALL privileges ON table test_table TO $SPIFFE_USER;
            GRANT ALL privileges ON sequence test_table_id_seq TO $SPIFFE_USER;
        !!EOF
    ---
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: spiffe-helper
      namespace: postgresql-spiffe
    data:
      helper.conf: |
        agent_address = "/spiffe-workload-api/spire-agent.sock"
        cmd = "/usr/bin/psql"
        cmd_args = "-U postgres -h 127.0.0.1 -c \"SELECT pg_reload_conf();\""
        cert_dir = "/opt/postgresql-certs"
        renew_signal = ""
        svid_file_name = "svid.pem"
        svid_key_file_name = "svid.key"
        svid_bundle_file_name = "svid_bundle.pem"
    ---
    kind: Service
    apiVersion: v1
    metadata:
      name: postgresql-spiffe
      namespace: postgresql-spiffe
    spec:
      ports:
        - protocol: TCP
          port: 5432
          targetPort: 5432
      type: ClusterIP
      selector:
        app: postgresql-spiffe
    ---
    kind: Deployment
    apiVersion: apps/v1
    metadata:
      name: postgresql-spiffe
      namespace: postgresql-spiffe
      labels:
        app: postgresql-spiffe
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: postgresql-spiffe
      template:
        metadata:
          labels:
            app: postgresql-spiffe
        spec:
          serviceAccountName: postgresql-spiffe
          securityContext:
            runAsNonRoot: true
            seccompProfile:
              type: RuntimeDefault
          initContainers:
            - name: spiffe-helper-init
              image: <registry>/spiffe-helper-postgresql:latest
              args:
                - '-config'
                - /etc/spiffe-helper/helper.conf
                - '-daemon-mode=false'
              volumeMounts:
                - name: spiffe-workload-api
                  readOnly: true
                  mountPath: /spiffe-workload-api
                - name: postgresql-certs
                  mountPath: /opt/postgresql-certs
                - name: spiffe-helper
                  mountPath: /etc/spiffe-helper
              securityContext:
                capabilities:
                  drop:
                    - ALL
          containers:
            - name: postgresql-spiffe
              image: registry.redhat.io/rhel9/postgresql-16:latest
              env:
                - name: POSTGRESQL_USER
                  value: user
                - name: POSTGRESQL_PASSWORD
                  value: wearenotusingthissoIdontworryaboutit
                - name: SPIFFE_USER
                  value: postgresql_spiffe
                - name: SPIFFE_PASSWORD
                  value: somealsonotusedpassword
                - name: SPIFFE_DATABASE
                  value: testdb
                - name: POSTGRESQL_DATABASE
                  value: sampledb
              ports:
                - name: postgresql
                  containerPort: 5432
                  protocol: TCP
              volumeMounts:
                - name: postgresql-certs
                  mountPath: /opt/postgresql-certs
                - name: pg-hba
                  mountPath: /opt/pg_hba
                - name: postgresql-init-db
                  mountPath: /opt/app-root/src/postgresql-init
                - name: postgres-config
                  mountPath: /opt/app-root/src/postgresql-cfg
              securityContext:
                capabilities:
                  drop:
                    - ALL
            - name: spiffe-helper
              image: <registry>/spiffe-helper-postgresql:latest
              args:
                - '-config'
                - /etc/spiffe-helper/helper.conf
              volumeMounts:
                - name: spiffe-workload-api
                  readOnly: true
                  mountPath: /spiffe-workload-api
                - name: postgresql-certs
                  mountPath: /opt/postgresql-certs
                - name: spiffe-helper
                  mountPath: /etc/spiffe-helper
              securityContext:
                capabilities:
                  drop:
                    - ALL
          volumes:
            - name: spiffe-workload-api
              csi:
                driver: csi.spiffe.io
                readOnly: true
            - name: postgresql-certs
              emptyDir:
                medium: Memory
            - name: spiffe-helper
              configMap:
                name: spiffe-helper
            - name: postgresql-init-db
              configMap:
                name: postgresql-init-db
            - name: pg-hba
              configMap:
                name: postgres-config
                items:
                  - key: pg_hba.conf
                    path: pg_hba.conf
            - name: postgres-config
              configMap:
                name: postgres-config
                items:
                  - key: postgresql.conf
                    path: postgresql.conf
    EOF
    ```

    Replace both `<registry>` occurrences in the deployment with your container registry.

4.  Confirm that the SPIFFE Helper configuration matches the PostgreSQL TLS settings by running the following command:

    ``` terminal
    $ oc get configmap spiffe-helper -n postgresql-spiffe \
      -o jsonpath='{.data.helper\.conf}{"\n"}'
    ```

    The `cert_dir` and `svid_*` file names must match the `ssl_*_file` paths in `postgresql.conf`. The server `helper.conf` must include settings similar to the following example:

    ``` terminal
    agent_address = "/spiffe-workload-api/spire-agent.sock"
    cmd = "/usr/bin/psql"
    cmd_args = "-U postgres -h 127.0.0.1 -c \"SELECT pg_reload_conf();\""
    cert_dir = "/opt/postgresql-certs"
    renew_signal = ""
    svid_file_name = "svid.pem"
    svid_key_file_name = "svid.key"
    svid_bundle_file_name = "svid_bundle.pem"
    ```

5.  Create the PostgreSQL client by using the following example. The client uses the stock SPIFFE Helper image from the Zero Trust Workload Identity Manager. Only the server deployment requires the custom image with the `psql` client.

    ``` yaml
    $ oc apply -f - << 'EOF'
    ---
    kind: Namespace
    apiVersion: v1
    metadata:
      name: postgresql-spiffe-client
    ---
    kind: ServiceAccount
    apiVersion: v1
    metadata:
      name: postgresql-spiffe-client
      namespace: postgresql-spiffe-client
    ---
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: spiffe-helper
      namespace: postgresql-spiffe-client
    data:
      helper.conf: |
        agent_address = "/spiffe-workload-api/spire-agent.sock"
        cmd = ""
        cmd_args = ""
        cert_dir = "/opt/postgresql-certs"
        renew_signal = ""
        svid_file_name = "svid.pem"
        svid_key_file_name = "svid.key"
        svid_bundle_file_name = "svid_bundle.pem"
    ---
    apiVersion: spire.spiffe.io/v1alpha1
    kind: ClusterSPIFFEID
    metadata:
      name: postgresql-spiffe-client
    spec:
      className: zero-trust-workload-identity-manager-spire
      dnsNameTemplates:
        - postgresql-spiffe
      namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: postgresql-spiffe-client
      podSelector:
        matchLabels:
          app: postgresql-spiffe-client
      spiffeIDTemplate: 'spiffe://{{ .TrustDomain }}/ns/{{ .PodMeta.Namespace }}/sa/{{ .PodSpec.ServiceAccountName }}'
    ---
    kind: Deployment
    apiVersion: apps/v1
    metadata:
      name: postgresql-spiffe-client
      namespace: postgresql-spiffe-client
      labels:
        app: postgresql-spiffe-client
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: postgresql-spiffe-client
      template:
        metadata:
          labels:
            app: postgresql-spiffe-client
        spec:
          serviceAccountName: postgresql-spiffe-client
          securityContext:
            runAsNonRoot: true
            seccompProfile:
              type: RuntimeDefault
          containers:
            - name: postgresql-spiffe-client
              image: registry.redhat.io/rhel9/postgresql-16:latest
              command:
                - /bin/bash
                - '-c'
                - sleep infinity
              volumeMounts:
                - name: postgresql-certs
                  mountPath: /opt/postgresql-certs
              securityContext:
                capabilities:
                  drop:
                    - ALL
            - name: spiffe-helper
              image: registry.redhat.io/zero-trust-workload-identity-manager/spiffe-helper-rhel9:
              args:
                - '-config'
                - /etc/spiffe-helper/helper.conf
              volumeMounts:
                - name: spiffe-workload-api
                  readOnly: true
                  mountPath: /spiffe-workload-api
                - name: postgresql-certs
                  mountPath: /opt/postgresql-certs
                - name: spiffe-helper
                  mountPath: /etc/spiffe-helper
              securityContext:
                capabilities:
                  drop:
                    - ALL
          volumes:
            - name: spiffe-workload-api
              csi:
                driver: csi.spiffe.io
                readOnly: true
            - name: postgresql-certs
              emptyDir:
                medium: Memory
            - name: spiffe-helper
              configMap:
                name: spiffe-helper
    EOF
    ```

    Replace `<version>` with the tag that matches your Zero Trust Workload Identity Manager installation.

6.  Confirm that pods are running in both namespaces by running the following commands:

    ``` terminal
    $ oc get pods -n postgresql-spiffe
    ```

    ``` terminal
    $ oc get pods -n postgresql-spiffe-client
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Inspect the server certificate by running the following command:

    ``` terminal
    $ oc rsh -n postgresql-spiffe -c postgresql-spiffe \
      deployment/postgresql-spiffe \
      cat /opt/postgresql-certs/svid.pem | openssl x509 -noout -text
    ```

    The server certificate should include the service hostname `postgresql-spiffe.postgresql-spiffe.svc`.

2.  Inspect the client certificate by running the following command:

    ``` terminal
    $ oc rsh -n postgresql-spiffe-client -c postgresql-spiffe-client \
      deployment/postgresql-spiffe-client \
      cat /opt/postgresql-certs/svid.pem | openssl x509 -noout -text
    ```

    The certificate common name (CN) field should be `postgresql_spiffe`.

3.  Connect to PostgreSQL from the client pod by running the following commands:

    ``` terminal
    $ oc rsh -n postgresql-spiffe-client -c postgresql-spiffe-client \
      deployment/postgresql-spiffe-client
    ```

    ``` terminal
    $ psql "host=postgresql-spiffe.postgresql-spiffe.svc port=5432 \
      user=postgresql_spiffe dbname=testdb sslmode=verify-full \
      sslcert=/opt/postgresql-certs/svid.pem \
      sslkey=/opt/postgresql-certs/svid.key \
      sslrootcert=/opt/postgresql-certs/svid_bundle.pem"
    ```

    If the deployment succeeded, `psql` connects to the database.

</div>

# SPIFFE Helper image reference

Reference information for the SPIFFE Helper container image included with the Zero Trust Workload Identity Manager, including image location, command-line flags, configuration options, and volume requirements.

## Image location

The Zero Trust Workload Identity Manager provides a SPIFFE Helper image at the following location:

``` text
registry.redhat.io/zero-trust-workload-identity-manager/spiffe-helper-rhel9:<version>
```

Replace `<version>` with the tag that matches your Zero Trust Workload Identity Manager installation. Some workloads require additional tools in the helper image.

## Command-line flags

| Flag | Description |
|----|----|
| `-config <path>` | Path to the SPIFFE Helper configuration file. Required. |
| `-daemon-mode <boolean>` | Controls operating mode. `true` (default) runs continuously and renews credentials. `false` fetches once and exits. |
| `-version` | Prints version information and exits. |

<div class="formalpara">

<div class="title">

Examples of command-line flags

</div>

``` terminal
$ spiffe-helper -config /etc/spiffe-helper/helper.conf
$ spiffe-helper -config /etc/spiffe-helper/helper.conf -daemon-mode=false
```

</div>

## Configuration file options

SPIFFE Helper reads a configuration file. The following table describes the most common options for X.509 workloads on OpenShift Container Platform.

| Option | Description |
|----|----|
| `agent_address` | Path to the SPIFFE Runtime Environment Agent Workload API socket. On Linux, SPIFFE Helper connects with `unix://<path>`. With the SPIFFE CSI driver, use `/spiffe-workload-api/spire-agent.sock`. You can also set the `SPIFFE_ENDPOINT_SOCKET` environment variable. |
| `cert_dir` | Directory where SPIFFE Helper writes credential files. The directory must exist before SPIFFE Helper starts. |
| `daemon_mode` | When `true` (default), runs continuously. When `false`, fetches once and exits. Can also be controlled with the `-daemon-mode` flag. |
| `svid_file_name`, `svid_key_file_name`, `svid_bundle_file_name` | File names for the X.509 SVID certificate, private key, and trust bundle. All three are required to enable X.509 output. |
| `jwt_bundle_file_name` | File name for a JWT bundle JSON file. |
| `jwt_svids` | Block defining JWT SVID audiences and output file names. |
| `cmd` | Executable path for the managed-child pattern. On the first successful X.509 write, SPIFFE Helper starts this process. Ignored in non-daemon mode. |
| `cmd_args` | Space-separated arguments for `cmd`. Use quoted strings for arguments that contain spaces. Not parsed by a shell unless you start a shell explicitly, for example `/bin/sh -c "…​"`. |
| `pid_file_name` | Path to a file containing one integer PID for the external-process pattern. Requires `renew_signal`. Invalid in non-daemon mode. |
| `renew_signal` | POSIX signal name sent on renewal, for example `SIGUSR1` or `SIGHUP`. Required when `pid_file_name` is set. Optional with `cmd`; when empty and `cmd` is set, later renewals do not signal the child. |
| `health_checks` | Optional HTTP liveness and readiness endpoints. Available in daemon mode only. |

## Volume and mount requirements

When deploying SPIFFE Helper on OpenShift Container Platform, mount the following resources:

| Volume | Mount path | Access |
|----|----|----|
| SPIFFE Workload API (CSI) | `/spiffe-workload-api` (or path matching `agent_address`) | Read-only |
| SPIFFE Helper configuration (`ConfigMap`) | Path passed to `-config`, for example `/etc/spiffe-helper/helper.conf` | Read-only |
| Certificate directory (`emptyDir` or persistent volume) | Path matching `cert_dir`, for example `/opt/postgresql-certs` or `/certs` | Read/write for the helper; read-only for the application container when possible |

<div class="formalpara">

<div class="title">

CSI volume example

</div>

``` yaml
apiVersion: apps/v1
metadata:
  name: postgresql-spiffe-client
  namespace: postgresql-spiffe-client
  labels:
    app: postgresql-spiffe-client
# ...
volumes:
- name: spiffe-workload-api
  csi:
    driver: csi.spiffe.io
    readOnly: true
```

</div>

<div class="formalpara">

<div class="title">

Init and sidecar container example

</div>

``` yaml
apiVersion: apps/v1
metadata:
  name: postgresql-spiffe
  namespace: postgresql-spiffe
  labels:
    app: postgresql-spiffe
# ...
initContainers:
- name: spiffe-helper-init
  image: registry.redhat.io/zero-trust-workload-identity-manager/spiffe-helper-rhel9:<version>
  args:
  - '-config'
  - /etc/spiffe-helper/helper.conf
  - '-daemon-mode=false'
  volumeMounts:
  - name: spiffe-workload-api
    readOnly: true
    mountPath: /spiffe-workload-api
  - name: postgresql-certs
    mountPath: /opt/postgresql-certs
  - name: spiffe-helper
    mountPath: /etc/spiffe-helper
containers:
- name: spiffe-helper
  image: registry.redhat.io/zero-trust-workload-identity-manager/spiffe-helper-rhel9:<version>
  args:
  - '-config'
  - /etc/spiffe-helper/helper.conf
  volumeMounts:
  - name: spiffe-workload-api
    readOnly: true
    mountPath: /spiffe-workload-api
  - name: postgresql-certs
    mountPath: /opt/postgresql-certs
  - name: spiffe-helper
    mountPath: /etc/spiffe-helper
```

</div>

<div class="formalpara">

<div class="title">

SPIFFE Helper configuration example

</div>

``` text
agent_address = "/spiffe-workload-api/spire-agent.sock"
cert_dir = "/opt/postgresql-certs"
svid_file_name = "svid.pem"
svid_key_file_name = "svid.key"
svid_bundle_file_name = "svid_bundle.pem"
cmd = "/usr/bin/psql"
cmd_args = "-U postgres -h 127.0.0.1 -c \"SELECT pg_reload_conf();\""
renew_signal = ""
```

</div>

Replace `<version>` with the tag that matches your Zero Trust Workload Identity Manager installation.

## Quick reference

| Question | Answer |
|----|----|
| What happens if both `cmd` and `pid_file_name` are set? | SPIFFE Helper writes files, then runs managed-child logic, then PID-file logic. There is no priority between them. |
| Is `renew_signal` required for `pid_file_name`? | Yes. Validation fails if `pid_file_name` is set without `renew_signal`. |
| Does SPIFFE Helper watch files for the application? | No. The application watches disk, polls, reads at connection time, or handles signals. |
| What happens in non-daemon mode? | SPIFFE Helper fetches once, writes files, and exits. No watching, `cmd`, or signals. |
| What triggers workload notification? | Only X.509 updates in daemon mode. JWT-only refreshes write files only. |
| Can SPIFFE Helper signal another container in the same pod? | Not by default. Containers use separate process namespaces unless `shareProcessNamespace: true` is set. |

# Troubleshooting SPIFFE Helper deployments

Resolve common issues when deploying the SPIFFE Helper image with Zero Trust Workload Identity Manager, and use the diagnostic `oc` commands to verify readiness, sidecars, and on-disk SVID certificates.

## Common issues

Certificate output directory is empty
SPIFFE Helper cannot reach the Workload API, cannot write to `cert_dir`, or the workload is not registered with SPIFFE Runtime Environment. Confirm the `ZeroTrustWorkloadIdentityManager` custom resource reports `Ready`, the CSI volume is mounted at the path in `agent_address`, and a matching `ClusterSPIFFEID` exists for the pod namespace and labels. Verify `cert_dir` exists before SPIFFE Helper starts; an `emptyDir` volume satisfies this requirement.

Init container exits but TLS files are missing
The init container must run with `-daemon-mode=false`. Check init container logs. If SPIFFE Helper reports configuration warnings about ignored `cmd` or `renew_signal`, that is expected in non-daemon mode. Ensure the certificate volume is shared with the main application container.

Sidecar runs but certificates are not renewed
Confirm the sidecar container does not set `-daemon-mode=false`. Check sidecar logs for Workload API or write errors. If writes fail, SPIFFE Helper logs the error and does not run `cmd` or PID-file notification logic.

Application does not pick up renewed certificates
SPIFFE Helper overwrites files in `cert_dir`; it does not notify your application unless you configure `cmd`, `pid_file_name`, or the application watches or polls the directory. For sidecar deployments with empty `cmd`, the application must reload TLS from disk. For PostgreSQL, configure the managed-child pattern with `psql` and `pg_reload_conf()` in the server sidecar.

`cmd` or `renew_signal` appears to have no effect
In non-daemon mode, SPIFFE Helper ignores `cmd` and `renew_signal`. In daemon mode, `cmd` and PID-file logic run only after a successful X.509 write. JWT bundle or JWT SVID updates do not trigger them. If `renew_signal` is empty while `cmd` is set, the child starts on first write but later renewals send no signal.

Cannot signal the application container from the helper sidecar
Containers in the same pod use separate process namespaces by default. `pid_file_name` and `cmd` cannot signal another container unless you set `shareProcessNamespace: true` or run the reload command as a child of SPIFFE Helper. The PostgreSQL example uses `cmd` to run `psql` locally instead of signaling the database container.

Configuration validation fails for `pid_file_name`
`renew_signal` is required when `pid_file_name` is set. `pid_file_name` is not valid in non-daemon mode.

Workload API socket is not accessible
Verify the CSI volume is mounted and the socket path matches `agent_address`, typically `/spiffe-workload-api/spire-agent.sock`. Confirm the Zero Trust Workload Identity Manager operands are running and the pod service account matches the `ClusterSPIFFEID` selectors.

Permission denied when reading certificate files
Check file ownership and permissions on the shared volume. Consider setting `fsGroup` in the pod `securityContext` so the application container can read files written by SPIFFE Helper. Mount the certificate directory read-only in the application container when possible.

Image pull errors for the SPIFFE Helper image
Confirm your cluster can pull `registry.redhat.io/zero-trust-workload-identity-manager/spiffe-helper-rhel9:<version>`. If you use a custom image, verify the registry credentials and image reference in the deployment manifest.

PostgreSQL mTLS connection fails after deployment
Confirm SPIFFE Helper wrote files to `/opt/postgresql-certs`, the client certificate CN matches the PostgreSQL user, and `pg_hba.conf` requires certificate authentication. Compare server and client SVIDs with `openssl x509 -noout -text`.

Use the following `oc` commands when investigating SPIFFE Helper deployments and workloads such as PostgreSQL.

## Verify Zero Trust Workload Identity Manager readiness

``` terminal
$ oc get ZeroTrustWorkloadIdentityManager cluster \
  -o jsonpath='{.status.conditions[?(@.type=="Ready")].status}{"\n"}'
```

``` terminal
$ oc get clusterspiffeid
```

## Inspect SPIFFE Helper pods

``` terminal
$ oc get pods -n postgresql-spiffe
```

``` terminal
$ oc get pods -n postgresql-spiffe-client
```

## Review SPIFFE Helper logs

``` terminal
$ oc logs -n postgresql-spiffe deployment/postgresql-spiffe -c spiffe-helper-init
```

``` terminal
$ oc logs -n postgresql-spiffe deployment/postgresql-spiffe -c spiffe-helper
```

``` terminal
$ oc logs -n postgresql-spiffe-client deployment/postgresql-spiffe-client -c spiffe-helper
```

## Verify on-disk SVID certificates

``` terminal
$ oc rsh -n postgresql-spiffe deployment/postgresql-spiffe -c postgresql-spiffe \
  -- ls -la /opt/postgresql-certs
```

``` terminal
$ oc rsh -n postgresql-spiffe deployment/postgresql-spiffe -c postgresql-spiffe -- \
  cat /opt/postgresql-certs/svid.pem | openssl x509 -noout -dates -subject
```
