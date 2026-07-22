<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use advanced Security Profiles Operator tasks to enable metrics, configure webhooks, or restrict syscalls.

# Restrict the allowed syscalls in seccomp profiles

The Security Profiles Operator does not restrict `syscalls` in `seccomp` profiles by default. You can define the list of allowed `syscalls` in the `spod` configuration.

> [!IMPORTANT]
> The Operator will install only the `seccomp` profiles, which have a subset of `syscalls` defined into the allowed list. All profiles not complying with this ruleset are rejected.
>
> When the list of allowed `syscalls` is modified in the `spod` configuration, the Operator will identify the already installed profiles which are noncompliant and remove them automatically.

<div>

<div class="title">

Procedure

</div>

- To define the list of `allowedSyscalls`, adjust the `spec` parameter by running the following command:

  ``` terminal
  $ oc -n openshift-security-profiles patch spod spod --type merge \
      -p '{"spec":{"allowedSyscalls": ["exit", "exit_group", "futex", "nanosleep"]}}'
  ```

</div>

# Base syscalls for a container runtime

You can use the `baseProfileName` attribute to establish the minimum required `syscalls` for a given runtime to start a container.

<div>

<div class="title">

Procedure

</div>

- Edit the `SeccompProfile` kind object and add `baseProfileName: runc-v1.0.0` to the `spec` field:

  ``` yaml
  apiVersion: security-profiles-operator.x-k8s.io/v1beta1
  kind: SeccompProfile
  metadata:
    name: example-name
  spec:
    defaultAction: SCMP_ACT_ERRNO
    baseProfileName: runc-v1.0.0
    syscalls:
      - action: SCMP_ACT_ALLOW
        names:
          - exit_group
  ```

</div>

# Enabling memory optimization in the spod daemon

The controller running inside of `spod` daemon process watches all pods available in the cluster when profile recording is enabled. This can lead to very high memory usage in large clusters, resulting in the `spod` daemon running out of memory or crashing.

To prevent crashes, the `spod` daemon can be configured to only load the pods labeled for profile recording into the cache memory.

> [!NOTE]
> SPO memory optimization is not enabled by default.

<div>

<div class="title">

Procedure

</div>

1.  Enable memory optimization by running the following command:

    ``` terminal
    $ oc -n openshift-security-profiles patch spod spod --type=merge -p '{"spec":{"enableMemoryOptimization":true}}'
    ```

2.  To record a security profile for a pod, the pod must be labeled with `spo.x-k8s.io/enable-recording: "true"`:

    ``` yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: my-recording-pod
      labels:
        spo.x-k8s.io/enable-recording: "true"
    # ...
    ```

</div>

# Customizing daemon resource requirements

The default resource requirements of the daemon container can be adjusted by using the field `daemonResourceRequirements` from the `spod` configuration.

<div>

<div class="title">

Procedure

</div>

- To specify the memory and cpu requests and limits of the daemon container, run the following command:

  ``` terminal
  $ oc -n openshift-security-profiles patch spod spod --type merge -p \
      '{"spec":{"daemonResourceRequirements": { \
      "requests": {"memory": "256Mi", "cpu": "250m"}, \
      "limits": {"memory": "512Mi", "cpu": "500m"}}}}'
  ```

</div>

# Setting a custom priority class name for the spod daemon pod

The default priority class name of the `spod` daemon pod is set to `system-node-critical`. A custom priority class name can be configured in the `spod` configuration by setting a value in the `priorityClassName` field.

<div>

<div class="title">

Procedure

</div>

- Configure the priority class name by running the following command:

  ``` terminal
  $ oc -n openshift-security-profiles patch spod spod --type=merge -p '{"spec":{"priorityClassName":"my-priority-class"}}'
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  securityprofilesoperatordaemon.openshift-security-profiles.x-k8s.io/spod patched
  ```

  </div>

</div>

# Using metrics

The `openshift-security-profiles` namespace provides metrics endpoints, which are secured by the `kube-rbac-proxy` container. All metrics are exposed by the `metrics` service within the `openshift-security-profiles` namespace.

The Security Profiles Operator includes a cluster role and corresponding binding `spo-metrics-client` to retrieve the metrics from within the cluster. There are two metrics paths available:

- `metrics.openshift-security-profiles/metrics`: for controller runtime metrics

- `metrics.openshift-security-profiles/metrics-spod`: for the Operator daemon metrics

<div>

<div class="title">

Procedure

</div>

1.  To view the status of the metrics service, run the following command:

    ``` terminal
    $ oc get svc/metrics -n openshift-security-profiles
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME      TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
    metrics   ClusterIP   10.0.0.228   <none>        443/TCP   43s
    ```

    </div>

2.  To retrieve the metrics, query the service endpoint using the default `ServiceAccount` token in the `openshift-security-profiles` namespace by running the following command:

    ``` terminal
    $ oc run --rm -i --restart=Never --image=registry.fedoraproject.org/fedora-minimal:latest \
        -n openshift-security-profiles metrics-test -- bash -c \
        'curl -ks -H "Authorization: Bearer $(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" https://metrics.openshift-security-profiles/metrics-spod'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    # HELP security_profiles_operator_seccomp_profile_total Counter about seccomp profile operations.
    # TYPE security_profiles_operator_seccomp_profile_total counter
    security_profiles_operator_seccomp_profile_total{operation="delete"} 1
    security_profiles_operator_seccomp_profile_total{operation="update"} 2
    ```

    </div>

3.  To retrieve metrics from a different namespace, link the `ServiceAccount` to the `spo-metrics-client` `ClusterRoleBinding` by running the following command:

    ``` terminal
    $ oc get clusterrolebinding spo-metrics-client -o wide
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                 ROLE                             AGE   USERS   GROUPS   SERVICEACCOUNTS
    spo-metrics-client   ClusterRole/spo-metrics-client   35m                    openshift-security-profiles/default
    ```

    </div>

</div>

## controller-runtime metrics

The controller-runtime `metrics` and the DaemonSet endpoint `metrics-spod` provide a set of default metrics. Additional metrics are provided by the daemon, which are always prefixed with `security_profiles_operator_`.

| Metric key | Possible labels | Type | Purpose |
|----|----|----|----|
| `seccomp_profile_total` | `operation={delete,update}` | Counter | Amount of seccomp profile operations. |
| `seccomp_profile_audit_total` | `node`, `namespace`, `pod`, `container`, `executable`, `syscall` | Counter | Amount of seccomp profile audit operations. Requires the log enricher to be enabled. |
| `seccomp_profile_bpf_total` | `node`, `mount_namespace`, `profile` | Counter | Amount of seccomp profile bpf operations. Requires the bpf recorder to be enabled. |
| `seccomp_profile_error_total` | `reason={` `SeccompNotSupportedOnNode,` `InvalidSeccompProfile,` `CannotSaveSeccompProfile,` `CannotRemoveSeccompProfile,` `CannotUpdateSeccompProfile,` `CannotUpdateNodeStatus` `}` | Counter | Amount of seccomp profile errors. |
| `selinux_profile_total` | `operation={delete,update}` | Counter | Amount of SELinux profile operations. |
| `selinux_profile_audit_total` | `node`, `namespace`, `pod`, `container`, `executable`, `scontext`,`tcontext` | Counter | Amount of SELinux profile audit operations. Requires the log enricher to be enabled. |
| `selinux_profile_error_total` | `reason={` `CannotSaveSelinuxPolicy,` `CannotUpdatePolicyStatus,` `CannotRemoveSelinuxPolicy,` `CannotContactSelinuxd,` `CannotWritePolicyFile,` `CannotGetPolicyStatus` `}` | Counter | Amount of SELinux profile errors. |

Available controller-runtime metrics

# Using the log enricher

The Security Profiles Operator contains a log enrichment feature, which is disabled by default. The log enricher container runs with `privileged` permissions to read the audit logs from the local node. The log enricher runs within the host PID namespace, `hostPID`.

> [!IMPORTANT]
> The log enricher must have permissions to read the host processes.

<div>

<div class="title">

Procedure

</div>

1.  Patch the `spod` configuration to enable the log enricher by running the following command:

    ``` terminal
    $ oc -n openshift-security-profiles patch spod spod \
        --type=merge -p '{"spec":{"enableLogEnricher":true}}'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    securityprofilesoperatordaemon.security-profiles-operator.x-k8s.io/spod patched
    ```

    </div>

    > [!NOTE]
    > The Security Profiles Operator will re-deploy the `spod` daemon set automatically.

2.  View the audit logs by running the following command:

    ``` terminal
    $ oc -n openshift-security-profiles logs -f ds/spod log-enricher
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    I0623 12:51:04.257814 1854764 deleg.go:130] setup "msg"="starting component: log-enricher"  "buildDate"="1980-01-01T00:00:00Z" "compiler"="gc" "gitCommit"="unknown" "gitTreeState"="clean" "goVersion"="go1.16.2" "platform"="linux/amd64" "version"="0.4.0-dev"
    I0623 12:51:04.257890 1854764 enricher.go:44] log-enricher "msg"="Starting log-enricher on node: 127.0.0.1"
    I0623 12:51:04.257898 1854764 enricher.go:46] log-enricher "msg"="Connecting to local GRPC server"
    I0623 12:51:04.258061 1854764 enricher.go:69] log-enricher "msg"="Reading from file /var/log/audit/audit.log"
    2021/06/23 12:51:04 Seeked /var/log/audit/audit.log - &{Offset:0 Whence:2}
    ```

    </div>

</div>

## Using the log enricher to trace an application

You can use the Security Profiles Operator log enricher to trace an application.

<div>

<div class="title">

Procedure

</div>

1.  To trace an application, create a `SeccompProfile` logging profile:

    ``` yaml
    apiVersion: security-profiles-operator.x-k8s.io/v1beta1
    kind: SeccompProfile
    metadata:
      name: log
    spec:
      defaultAction: SCMP_ACT_LOG
    ```

2.  Create a pod object to use the profile:

    ``` yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: log-pod
      namespace: default
    spec:
      securityContext:
        runAsNonRoot: true
        seccompProfile:
          type: Localhost
          localhostProfile: operator/log.json
      containers:
      - name: log-container
        image: quay.io/security-profiles-operator/test-nginx-unprivileged:1.21
        securityContext:
          allowPrivilegeEscalation: false
          capabilities:
            drop: [ALL]
    ```

3.  Examine the log enricher output by running the following command:

    ``` terminal
    $ oc -n openshift-security-profiles logs -f ds/spod log-enricher
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    …
    I0623 12:59:11.479869 1854764 enricher.go:111] log-enricher "msg"="audit"  "container"="log-container" "executable"="/" "namespace"="default" "node"="127.0.0.1" "pid"=1905792 "pod"="log-pod" "syscallID"=3 "syscallName"="close" "timestamp"="1624453150.205:1061" "type"="seccomp"
    I0623 12:59:11.487323 1854764 enricher.go:111] log-enricher "msg"="audit"  "container"="log-container" "executable"="/" "namespace"="default" "node"="127.0.0.1" "pid"=1905792 "pod"="log-pod" "syscallID"=157 "syscallName"="prctl" "timestamp"="1624453150.205:1062" "type"="seccomp"
    I0623 12:59:11.492157 1854764 enricher.go:111] log-enricher "msg"="audit"  "container"="log-container" "executable"="/" "namespace"="default" "node"="127.0.0.1" "pid"=1905792 "pod"="log-pod" "syscallID"=157 "syscallName"="prctl" "timestamp"="1624453150.205:1063" "type"="seccomp"
    …
    I0623 12:59:20.258523 1854764 enricher.go:111] log-enricher "msg"="audit"  "container"="log-container" "executable"="/usr/sbin/nginx" "namespace"="default" "node"="127.0.0.1" "pid"=1905792 "pod"="log-pod" "syscallID"=12 "syscallName"="brk" "timestamp"="1624453150.235:2873" "type"="seccomp"
    I0623 12:59:20.263349 1854764 enricher.go:111] log-enricher "msg"="audit"  "container"="log-container" "executable"="/usr/sbin/nginx" "namespace"="default" "node"="127.0.0.1" "pid"=1905792 "pod"="log-pod" "syscallID"=21 "syscallName"="access" "timestamp"="1624453150.235:2874" "type"="seccomp"
    I0623 12:59:20.354091 1854764 enricher.go:111] log-enricher "msg"="audit"  "container"="log-container" "executable"="/usr/sbin/nginx" "namespace"="default" "node"="127.0.0.1" "pid"=1905792 "pod"="log-pod" "syscallID"=257 "syscallName"="openat" "timestamp"="1624453150.235:2875" "type"="seccomp"
    I0623 12:59:20.358844 1854764 enricher.go:111] log-enricher "msg"="audit"  "container"="log-container" "executable"="/usr/sbin/nginx" "namespace"="default" "node"="127.0.0.1" "pid"=1905792 "pod"="log-pod" "syscallID"=5 "syscallName"="fstat" "timestamp"="1624453150.235:2876" "type"="seccomp"
    I0623 12:59:20.363510 1854764 enricher.go:111] log-enricher "msg"="audit"  "container"="log-container" "executable"="/usr/sbin/nginx" "namespace"="default" "node"="127.0.0.1" "pid"=1905792 "pod"="log-pod" "syscallID"=9 "syscallName"="mmap" "timestamp"="1624453150.235:2877" "type"="seccomp"
    I0623 12:59:20.454127 1854764 enricher.go:111] log-enricher "msg"="audit"  "container"="log-container" "executable"="/usr/sbin/nginx" "namespace"="default" "node"="127.0.0.1" "pid"=1905792 "pod"="log-pod" "syscallID"=3 "syscallName"="close" "timestamp"="1624453150.235:2878" "type"="seccomp"
    I0623 12:59:20.458654 1854764 enricher.go:111] log-enricher "msg"="audit"  "container"="log-container" "executable"="/usr/sbin/nginx" "namespace"="default" "node"="127.0.0.1" "pid"=1905792 "pod"="log-pod" "syscallID"=257 "syscallName"="openat" "timestamp"="1624453150.235:2879" "type"="seccomp"
    …
    ```

    </div>

</div>

# Configuring webhooks

Profile binding and profile recording objects can use webhooks. Profile binding and recording object configurations are `MutatingWebhookConfiguration` CRs, managed by the Security Profiles Operator.

To change the webhook configuration, the `spod` CR exposes a `webhookOptions` field that allows modification of the `failurePolicy`, `namespaceSelector`, and `objectSelector` variables. This allows you to set the webhooks to "soft-fail" or restrict them to a subset of a namespaces so that even if the webhooks failed, other namespaces or resources are not affected.

<div>

<div class="title">

Procedure

</div>

1.  Set the `recording.spo.io` webhook configuration to record only pods labeled with `spo-record=true` by creating the following patch file:

    ``` yaml
    spec:
      webhookOptions:
        - name: recording.spo.io
          objectSelector:
            matchExpressions:
              - key: spo-record
                operator: In
                values:
                  - "true"
    ```

2.  Patch the `spod/spod` instance by running the following command:

    ``` terminal
    $ oc -n openshift-security-profiles patch spod \
        spod -p $(cat /tmp/spod-wh.patch) --type=merge
    ```

3.  To view the resulting `MutatingWebhookConfiguration` object, run the following command:

    ``` terminal
    $ oc get MutatingWebhookConfiguration \
        spo-mutating-webhook-configuration -oyaml
    ```

</div>
