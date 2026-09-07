<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

With the Advanced Audit Logging Framework in the OpenShift Container Platform Security Profiles Operator (SPO), you can correlate cluster users with actions during `oc exec`, `oc rsh`, and `oc debug` sessions.

The Advanced Audit Logging Framework in SPO 0.10.0 logs activity from an Red Hat Enterprise Linux CoreOS (RHCOS) container back to the hosting cluster and produces detailed logs in a JSON Lines format.

# Benefits of the Advanced Audit Logging Framework

The `kubectl exec`, `oc exec`, `oc rsh` and `oc debug` commands do not pass user authentication details into the exec session on the container, making it hard to correlate Kubernetes user actions caused by actions on the host. The audit logger in SPO addresses this with mutating webhooks that inject the request UID from the Kubernetes API server as an environment variable into the session. Every request to the API server including the request to start a new exec session has a request UID. This request UID is then logged by the Advanced Audit Logging Framework. The request ID is used to correlate the activity with the API server audit logs, providing an audit trail within the node.

With the addition of the Advanced Audit Logging Framework, SPO now has two use cases:

- Pod auditing

- Node auditing

The use of privileged `seccompProfile` configuration is required only for the case of node auditing.

> [!NOTE]
> The Security Profiles Operator supports only Red Hat Enterprise Linux CoreOS (RHCOS) worker nodes appropriate to the version of OpenShift Container Platform in use.
>
> Red Hat Enterprise Linux (RHEL) nodes are not supported.

# Performance considerations

It is important to consider the performance cost of using seccomp profiles for extensive logging. SPO is designed to minimize this impact by primarily logging only process creations and handling them asynchronously. This approach helps prevent logging from becoming a bottleneck on your nodes.

The Advanced Audit Logging feature uses eBPF as a supplemental data source. While it is possible for eBPF to be used as a primary data source for this type of logging, that functionality is not currently a configurable feature within the Operator. For most use cases, the default asynchronous, process-creation-focused logging approach provides an excellent balance between security visibility and cluster performance.

# Prerequisites for the Advanced Audit Logging Framework

Before enabling the Advanced Audit Logging Framework, ensure the following requirements are met.

Security Profiles Operator version 0.10.0 or later is installed. The Advanced Audit Logging Framework requires Security Profiles Operator version 0.10.0 or later.

For node debugging sessions:

- To audit `oc debug` node sessions, CRI-O version 1.33 or later is required. It is available in OpenShift Container Platform 4.20 or later.

- The --privileged-seccomp-profile flag must be configured in CRI-O to apply `seccompProfiles` to privileged containers.

- The supported Linux used with the Advanced Audit Logging Framework is Red Hat Enterprise Linux CoreOS (RHCOS) running in a container in OpenShift Container Platform 4.20 or later.

If you are using the CRI-O runtime, you must configure it to allow `seccompProfile` to be applied to privileged containers. Add the following flag to your CRI-O runtime configuration: `--privileged-seccomp-profile=/var/lib/kubelet/seccomp/operator/profile1.json`. This is explained in more detail in the Advanced Audit Logging installation and enablement steps. The `--privileged-seccomp-profile` flag is available starting with OpenShift Container Platform 4.20 and later.

If you are using any version of SPO before 0.9.0, you must perform a migration procedure to install versions 0.9.0 or 0.10.0. The migration procedure converts SPO to operate on cluster-scoped resources.

First-time installation of SPO version 0.10.0 does not require migration. Also, if you are currently on SPO 0.9.0, you do not require migration and can directly upgrade to SPO 0.10.0.

> [!IMPORTANT]
> Do not attempt to upgrade directly from SPO versions before 0.9.0 to either 0.9.0 or 0.10.0 if you are currently running SPO. You must perform the migration procedure to convert SPO for operation at the cluster level.
>
> This change allows Advanced Audit Logging of events inside the worker node.
>
> This capability is not provided for control nodes since SPO does not operate on `etcd` nodes.

# The Audit JSON log enricher

The SPO Advanced Audit Logging Framework is enabled by the Audit JSON log enricher. Similar to the log enricher feature, the Audit JSON log enricher watches the `auditd` (`/var/log/audit/audit.log`) or the `syslog` (`/var/log/syslog`) daemons and generates a new audit log in JSON lines format.

Each JSON line includes the following:

- Timestamp: When the activity happened, shown in a standard ISO format

- Executable Name: The name of the program that was run (`bash`, `ls`).

- Linux Command Line Arguments (`cmdline`): The extra instructions given when the program was started (`ls -l /home`).

- User and Group IDs (`UID/GID`): The identification numbers of the system user who ran the program.

- System Calls (`syscalls`): A list of system calls (`syscalls`) that the process made

This log format and configuration is similar to how Kubernetes records audit logs. This is useful for:

- Seeing what users and automated processes are doing inside a pod.

- Tracking when someone uses commands such as `kubectl exec` to enter a running container and run commands or scripts.

- Monitoring activities in debug containers where users might run various tools.

# Kubernetes API log compared to Advanced Audit Logging output

To understand the value of Advanced Audit Logging, compare the Kubernetes API Server Audit Log to the Advanced Audit Logging output:

<div class="formalpara">

<div class="title">

Kubernetes API Server Audit Log

</div>

``` yaml
{
  "kind": "Event",
  "apiVersion": "audit.k8s.io/v1",
  "level": "Metadata",
  "auditID": "4d434cd4-xxxx-xxxx-xxxx-2d9aa46292ce",
  "stage": "ResponseComplete",
  "requestURI": "/api/v1/namespaces/test-namespace/pods/test-pod/exec?command=sh&command=-c&command=touch+/tmp/testfile.txt&container=nginx",
  "verb": "create",
  "user": {
    "username": "kube:admin",
    "groups": ["system:cluster-admins", "system:authenticated"]
  },
  "sourceIPs": ["xxx.xxx.xxx.xxx"],
  "userAgent": "oc/4.19.0 (linux/amd64)",
  "objectRef": {
    "resource": "pods",
    "namespace": "test-namespace",
    "name": "test-pod",
    "subresource": "exec"
  },
  "responseStatus": {
    "code": 101
  },
  "requestReceivedTimestamp": "2026-02-16T14:01:06.056518Z",
  "annotations": {
    "authorization.k8s.io/decision": "allow",
    "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding...",
    "execmetadata.spo.io/SPO_EXEC_REQUEST_UID": "aec3e0e1-xxxx-xxxx-xxxx-a7c58241f1a9"
  }
}
```

</div>

The correlation key is the `SPO_EXEC_REQUEST_UID` on the last line in the above file.

<div class="formalpara">

<div class="title">

Advanced Audit Logging Output

</div>

``` yaml
{
  "auditID": "d586679d-xxxx-xxxx-xxxx-9dc8ab273065",
  "cmdLine": "touch /tmp/testfile.txt ",        // Linux command with arguments
  "executable": "/bin/dash",
  "gid": 0,
  "node": {
    "name": "worker-1"
  },
  "pid": 144968,
  "requestUID": "aec3e0e1-xxxx-xxxx-xxxx-a7c58241f1a9", // Correlation key
  "resource": {
    "container": "nginx",
    "namespace": "test-namespace",
    "pod": "test-pod"
  },
  "syscalls": ["execve"],
  "timestamp": "2026-02-16T14:01:07.000Z",
  "uid": 0,
  "version": "spo/v1_alpha"
}
```

</div>

# Enabling Advanced Audit Logging

To enable Advanced Audit Logging, configure the Audit JSON log enricher and specify a set of filters to only log user activity.

<div>

<div class="title">

Procedure

</div>

1.  Enable the JSON enricher by running the following command:

    ``` terminal
    # kubectl -n openshift-security-profiles patch spod spod --type=merge -p '{"spec":{"enableJsonEnricher":true}}'
    ```

    Monitor the SPOD pods for correct restart and wait for all SPOD pods to show `Running` before proceeding.

2.  Check the pods for application of the change with the following command:

    ``` terminal
    $ oc get pods -n openshift-security-profiles -l name=spod -w
    ```

    Wait until all SPOD pods show `Running` before proceeding.

    > [!NOTE]
    > Each configuration change triggers a restart of the SPOD pods. After applying a patch, wait for all SPOD pods to return to the `Running` state before continuing.

    The Audit JSON log enricher uses eBPF as a supplemental data source. While processing `auditd` logs from `/var/log/audit/audit.log`, the enricher attempts to fetch ephemeral data from `/proc/<pid>` directories. Due to a race condition, these files might be deleted before they can be read. To ensure data completeness, the enricher falls back to fetching the necessary information from eBPF whenever it is not found in `/proc/<pid>`.

</div>

# Audit JSON Log Enricher configuration

Configure the Audit JSON Log Enricher to set the audit log interval, destination, and file path so Advanced Audit Logging records are written on a schedule and to a location you can collect and review.

> [!NOTE]
> Each configuration change triggers a restart of the SPOD pods. After applying a patch, wait for all SPOD pods to return to the `Running` state before continuing.

Setting the audit log interval determines how often audit logs are created using the `auditLogIntervalSeconds` option.

<div>

<div class="title">

Procedure

</div>

1.  Configure the audit log interval to 30 seconds by using the following command:

    ``` terminal
    # kubectl -n openshift-security-profiles patch spod spod --type=merge -p '{"spec":{"enableJsonEnricher":true,"verbosity":0,"jsonEnricherOptions":{"auditLogIntervalSeconds":30}}}'
    ```

    Wait until all SPOD pods show `Running` before proceeding. By default, audit logs go to your standard output in JSON lines format. You can send them to a file instead.

    Configure the Security Profiles Operator to store the log file on the node. Update the `security-profiles-operator-profile` `configmap` with two keys. This example YAML uses both keys to set up a host path volume at `/tmp/logs`.

2.  Create a file such as `patch-volume-source.json` that contains the following content:

    ``` json
    {
      "data": {
        "json-enricher-log-volume-mount-path": "/tmp/logs",
        "json-enricher-log-volume-source.json": "{\"hostPath\": {\"path\": \"/tmp/logs\",\"type\": \"DirectoryOrCreate\"}}"
      }
    }
    ```

    - `json-enricher-log-volume-source.json`: Defines the type of volume (for example, a host path and empty directory) where logs are stored. This value must be a JSON string that represents a `corev1.VolumeSource` object.

    - `json-enricher-log-volume-mount-path`: Specifies the directory path where the log file is generated.

3.  Verify the file contents by running the following command:

    ``` terminal
    $ cat patch-volume-source.json
    ```

4.  Update the `security-profiles-operator-profile` `configmap` by using the following command:

    ``` terminal
    # kubectl patch configmap security-profiles-operator-profile -n openshift-security-profiles --patch-file patch-volume-source.json
    ```

    Wait until all SPOD pods show `Running` before proceeding.

5.  Set the audit log file path by configuring the JSON log enricher with the full path to your audit log file, including the file name, by running the following command:

    ``` terminal
    # kubectl -n openshift-security-profiles patch spod spod --type=merge -p '{"spec":{"enableJsonEnricher":true,"verbosity":0,"jsonEnricherOptions":{"auditLogPath":"/tmp/logs/audit1.log"}}}'
    ```

    Wait until all SPOD pods show `Running` before proceeding.

</div>

# Audit log file fine-tuning and rotation

For audit logging to a file, you can manage file size and how long each file is kept. These options are similar to [Kubernetes API server log settings](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/).

<div>

<div class="title">

Procedure

</div>

1.  You configure these by patching the JSON log enricher options:

    ``` terminal
    # kubectl -n openshift-security-profiles patch spod spod --type=merge -p '{"spec":{"enableJsonEnricher":true,"verbosity":0,"jsonEnricherOptions":{"auditLogPath":"/tmp/logs/audit1.log","auditLogMaxSize":500,"auditLogMaxBackups":2,"auditLogMaxAge":10}}}'
    ```

    Wait until all SPOD pods show `Running` before proceeding.

    - `auditLogMaxSize`: The maximum size (in megabytes) a log file can reach before it’s rotated (a new file is started).

    - `auditLogMaxBackups`: The maximum number of older, rotated log files to keep. Set to 0 for no limit.

    - `auditLogMaxAge`: The maximum number of days to keep old log files.

2.  Increase the logging level for the JSON log enricher container to help with debugging. A value of `0` sets minimal logs. A value of `1` sets more detailed logs. You can choose either of these two levels and enable either level with the following command:

    ``` terminal
    # kubectl -n openshift-security-profiles patch spod spod --type=merge -p '{"spec":{"enableJsonEnricher":true, "verbosity": 1}}'
    ```

    Wait until all SPOD pods show `Running` before proceeding.

</div>

# Advanced audit logs for a specific pod

To log activity for a single pod, create a `SeccompProfile` that logs specific syscalls such as `execve`, and create a `ProfileBinding` that applies the profile to pods in a target namespace. The `SeccompProfile` applies cluster-wide. The `ProfileBinding` applies to workloads in that namespace.

Starting with OpenShift Container Platform 4.20 and CRI-O 1.33, you can apply a `SeccompProfile` to privileged containers. Add the `--privileged-seccomp-profile` flag to the CRI-O runtime configuration so that privileged debugging pods are also covered by the profile.

Bind the profile to a namespace to apply it to workloads. New pods in that namespace then receive the profile automatically.

<div>

<div class="title">

Procedure

</div>

1.  Create a file such as `profile1.yaml` with the following content:

    ``` yaml
    apiVersion: security-profiles-operator.x-k8s.io/v1beta1
    kind: SeccompProfile
    metadata:
      name: profile1
      namespace: openshift-security-profiles
    spec:
      defaultAction: SCMP_ACT_ALLOW
      syscalls:
      - action: SCMP_ACT_LOG
        names:
          - execve
          - clone
          - getpid
    ```

    This profile allows all normal actions (`defaultAction: SCMP_ACT_ALLOW`). It specifically tells the system to log when a process tries to run a new program (`execve`), create a new process (`clone`), or get its own process ID (`getpid`). These actions often indicate user interaction within a pod.

2.  Apply this `SeccompProfile` to your cluster by running the following command:

    ``` terminal
    # kubectl apply -f profile1.yaml
    ```

    > [!NOTE]
    > The Security Profiles Operator must use the privileged `SeccompProfile`.

3.  Create a file named `image_sec_comp.yaml` that contains the following YAML:

    ``` yaml
    apiVersion: security-profiles-operator.x-k8s.io/v1alpha1
    kind: ProfileBinding
    metadata:
      namespace: default
      name: all-pod-binding
    spec:
      profileRef:
        kind: SeccompProfile
        name: profile1
      image: "*"
    ```

4.  Apply the binding by running the following command:

    ``` terminal
    # kubectl apply -f image_sec_comp.yaml
    ```

5.  Label the namespace to activate the binding by running the following command:

    ``` terminal
    # kubectl label ns default spo.x-k8s.io/enable-binding=true
    ```

6.  Create a file such as `my-pod.yaml` that contains the following pod definition:

    ``` yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: my-pod
      labels:
        app: my-app
    spec:
      securityContext:
        seccompProfile:
          type: Localhost
          localhostProfile: operator/profile1.json
      containers:
        - name: nginx
          image: quay.io/security-profiles-operator/test-nginx:1.19.1
    ```

    - `type: Localhost` means you are using a profile that you defined in the cluster.

    - `localhostProfile: operator/profile1.json` tells the pod to use the `profile1` profile that you created. The `operator/` path is where the Security Profiles Operator stores these profiles.

7.  Apply the pod definition by running the following command:

    ``` terminal
    # kubectl apply -f my-pod.yaml
    ```

8.  Open a shell in the pod by running the following command:

    ``` terminal
    # kubectl exec -it my-pod -- /bin/sh
    ```

9.  Create an empty file in the pod by running the following command:

    ``` terminal
    # touch /tmp/audittest/demo-file
    ```

10. Stream the advanced audit log by running the following command:

    ``` terminal
    # kubectl -n openshift-security-profiles logs --since=1m --selector name=spod -c json-enricher --max-log-requests 6 -f
    ```

11. Identify the node where the pod runs by running the following command:

    ``` terminal
    # kubectl get pod my-pod -o wide
    ```

    The audit log file specified in the `auditLogPath` field is written to the file system on the node where the pod is running. To inspect the audit logs, access the node and open the file at the configured path, such as `/tmp/logs/audit1.log`.

12. Access the node by running the following command:

    ``` terminal
    $ sudo ssh core@<node_name>
    ```

13. View the audit log by running the following command:

    ``` terminal
    $ cat /tmp/logs/audit1.log
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    {
    "auditID": "a1b2c3d4-e5f6-7890-abcd-111111111111",
    "cmdLine": "mkdir /tmp/audittest ",
    "executable": "/bin/bash",
    "gid": 0,
    "node": {"name": "worker-1"},
    "pid": 27184,
    "requestUID": "f011c4a3-b20e-44ed-bb91-23e03ae31b3e",
    "resource": {
    "container": "nginx",
    "namespace": "default",
    "pod": "my-pod"
    },
    "syscalls": ["getpid", "execve"],
    "timestamp": "2026-02-16T06:34:53.000Z",
    "uid": 0,
    "version": "spo/v1_alpha"
    }
    {
    "auditID": "a1b2c3d4-e5f6-7890-abcd-222222222222",
    "cmdLine": "touch /tmp/audittest/demo-file ",
    "executable": "/bin/bash",
    "gid": 0,
    "node": {"name": "worker-1"},
    "pid": 27274,
    "requestUID": "f011c4a3-b20e-44ed-bb91-23e03ae31b3e",
    "resource": {
    "container": "nginx",
    "namespace": "default",
    "pod": "my-pod"
    },
    "syscalls": ["getpid", "execve"],
    "timestamp": "2026-02-16T06:35:02.000Z",
    "uid": 0,
    "version": "spo/v1_alpha"
    }
    ```

    </div>

</div>

# Monitor the audit logs

Monitor advanced audit logs from the `json-enricher` container, by streaming pod logs or by reading the audit log file on the node, so you can verify that Advanced Audit Logging is capturing session activity.

The audit log file is specified in the `auditLogPath` field and is written to the file system on the node where the pod is running. To inspect the audit logs, access the node and open the file at the configured path, such as `/tmp/logs/audit1.log`.

<div>

<div class="title">

Procedure

</div>

1.  Stream the advanced audit log by using the following command:

    ``` terminal
    # kubectl -n openshift-security-profiles logs --since=1m --selector name=spod -c json-enricher --max-log-requests 6 -f
    ```

2.  Identify the node on which the pod is scheduled by using the following command:

    ``` terminal
    # kubectl get pod my-pod -o wide
    ```

3.  Access the node by using the following command:

    ``` terminal
    $ sudo ssh core@<node_name>
    ```

4.  View the audit log by using the following command:

    ``` terminal
    $ cat /tmp/logs/audit1.log
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    {
    "auditID": "a1b2c3d4-e5f6-7890-abcd-111111111111",
    "cmdLine": "mkdir /tmp/audittest ",
    "executable": "/bin/bash",
    "gid": 0,
    "node": {"name": "worker-1"},
    "pid": 27184,
    "requestUID": "f011c4a3-b20e-44ed-bb91-23e03ae31b3e",
    "resource": {
    "container": "nginx",
    "namespace": "default",
    "pod": "my-pod"
    },
    "syscalls": ["getpid", "execve"],
    "timestamp": "2026-02-16T06:34:53.000Z",
    "uid": 0,
    "version": "spo/v1_alpha"
    }
    {
    "auditID": "a1b2c3d4-e5f6-7890-abcd-222222222222",
    "cmdLine": "touch /tmp/audittest/demo-file ",
    "executable": "/bin/bash",
    "gid": 0,
    "node": {"name": "worker-1"},
    "pid": 27274,
    "requestUID": "f011c4a3-b20e-44ed-bb91-23e03ae31b3e",
    "resource": {
    "container": "nginx",
    "namespace": "default",
    "pod": "my-pod"
    },
    "syscalls": ["getpid", "execve"],
    "timestamp": "2026-02-16T06:35:02.000Z",
    "uid": 0,
    "version": "spo/v1_alpha"
    }
    ```

    </div>

</div>

# Audit node debugging sessions

Enable privileged `seccomp` profiles in CRI-O so Advanced Audit Logging can record activity from `kubectl debug` and `oc debug` node sessions.

If you are using the CRI-O runtime, you must configure it to allow `seccomp` profiles on privileged containers by adding the `--privileged-seccomp-profile=/var/lib/kubelet/seccomp/operator/profile1.json` flag to your CRI-O runtime configuration.

> [!NOTE]
> The `--privileged-seccomp-profile` flag is available starting with OpenShift Container Platform 4.20 or later and CRI-O version 1.33 or later.

<div>

<div class="title">

Procedure

</div>

1.  SSH into the target node using the following command:

    ``` terminal
    # ssh core@<node_ip_address>
    ```

2.  Check to see if the files are there:

    ``` terminal
    # ls /var/lib/kubelet/seccomp/operator/
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    # kubelet-config.json  profile1.json
    ```

    </div>

3.  Stop the `kubelet` with the following commands:

    ``` terminal
    # systemctl stop kubelet
    ```

4.  Stop CRI-O with the command:

    ``` terminal
    # systemctl stop crio
    ```

5.  Set the CRI-O options with the following command:

    ``` terminal
    # echo "CRIO_CONFIG_OPTIONS --privileged-seccomp-profile=/var/lib/kubelet/seccomp/operator/profile1.json" > /etc/sysconfig/crio
    ```

6.  Now restart the kubelet with this command:

    ``` terminal
    # systemctl start kubelet
    ```

7.  Restart CRI-O with this command:

    ``` terminal
    # systemctl start crio
    ```

8.  To audit kubectl debug sessions, run the following command:

    ``` terminal
    # kubectl debug node/<node_name> -it --image=ubuntu -- bash
    ```

    Create the file on the container for the debugging information.

9.  `chroot` to the host with this command:

    ``` terminal
    # chroot /host
    ```

10. Go into the `/tmp` directory with this command:

    ``` terminal
    # cd /tmp
    ```

11. Create an empty file named `demonodedebug` with this command:

    ``` terminal
    # touch demonodedebug
    ```

12. Exit the node with the command:

    ``` terminal
    # exit
    ```

13. To monitor the logs, SSH to a node with this command:

    ``` terminal
    $ sudo ssh core@<node_name>
    ```

14. View the audit log using this command:

    ``` terminal
    $ cat /tmp/logs/audit1.log
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` yaml
    {
      "auditID": "edce381a-998d-4f3f-99d8-d0c4d0c8a613",
      "cmdLine": "touch demonodedebug",
      "executable": "/usr/bin/bash",
      "gid": 0,
      "node": {"name": "worker-1"},
      "pid": 99086,
      "resource": {
        "container": "container-00",
        "namespace": "openshift-security-profiles",
        "pod": "worker-1-debug"
      },
      "syscalls": ["execve", "getpid"],
      "timestamp": "2026-02-12T13:50:11.000Z",
      "uid": 0,
      "version": "spo/v1_alpha"
    }
    ```

    </div>

</div>

# Correlate with Kubernetes audit logs

Use the `requestUID` from the Security Profiles Operator (SPO) log to find the corresponding API server log entry, confirming who initiated the session.

<div>

<div class="title">

Procedure

</div>

1.  Start the pod by running the following command:

    ``` terminal
    $ oc exec my-pod -c nginx -- sh -c "touch /tmp/testfile.txt"
    ```

2.  Identify the node where the pod is running:

    ``` terminal
    $ NODE=$(oc get pod my-pod -o jsonpath='{.spec.nodeName}')
    ```

3.  Access the node and check the JSON enriched audit log using the following commands:

    ``` terminal
    # oc debug node/$NODE
    # chroot /host
    # grep "testfile" /tmp/logs/audit1.log | jq .
    ```

</div>

# Audit JSON Log Enricher output

For an exec session, the Audit JSON Log Enricher records two entries: the `SPO_EXEC_REQUEST_UID` injection and the command that ran on the pod. Match the shared `UID` value to connect the entries.

1.  The first listing is the container runtime wrapper.

    ``` yaml
    {
      "auditID": "062e2bd2-xxxx-xxxx-xxxx-57fb39d65a99",
      "cmdLine": "env SPO_EXEC_REQUEST_UID=aec3e0e1-xxxx-xxxx-xxxx-a7c58241f1a9 sh -c touch /tmp/testfile.txt ",
      "executable": "/usr/bin/crun",
      "pid": 144966,
      "requestUID": "aec3e0e1-xxxx-xxxx-xxxx-a7c58241f1a9",
      "resource": {
        "container": "nginx",
        "namespace": "default",
        "pod": "my-pod"
      },
      "node": {
        "name": "worker-1"
      },
      "syscalls": ["execve", "getpid", "clone"],
      "timestamp": "2026-02-16T14:01:07.000Z"
    }
    ```

2.  The second listing is the actual command executed.

    ``` yaml
    {
      "auditID": "d586679d-xxxx-xxxx-xxxx-9dc8ab273065",
      "cmdLine": "touch /tmp/testfile.txt ",
      "executable": "/bin/dash",
      "pid": 144968,
      "requestUID": "aec3e0e1-xxxx-xxxx-xxxx-a7c58241f1a9", // Correlation key
      "resource": {
        "container": "nginx",
        "namespace": "default",
        "pod": "my-pod"
      },
      "node": {
        "name": "worker-1"
      },
      "syscalls": ["execve"],
      "timestamp": "2026-02-16T14:01:07.000Z"
    }
    ```

3.  You can search the Kubernetes API audit log by using the `requestUID` with the following command:

    ``` terminal
    $ oc adm node-logs --role=master --path=kube-apiserver/audit.log | grep request_UID
    ```

# Kubernetes API audit log output

The Kubernetes API audit log output is YAML. It includes the `SPO_EXEC_REQUEST_UID` field that provides the correlation key for searching the Advanced Audit Logging output.

``` yaml
{
  "kind": "Event",
  "apiVersion": "audit.k8s.io/v1",
  "level": "Metadata",
  "auditID": "4d434cd4-xxxx-xxxx-xxxx-2d9aa46292ce",
  "stage": "ResponseComplete",
  "requestURI": "/api/v1/namespaces/test-namespace/pods/test-pod/exec?command=sh&command=-c&command=touch+/tmp/testfile.txt&container=nginx",
  "verb": "create",
  "user": {
    "username": "kube:admin",
    "groups": ["system:cluster-admins", "system:authenticated"]
  },
  "sourceIPs": ["xxx.xxx.xxx.xxx"],
  "userAgent": "oc/4.19.0 (linux/amd64)",
  "objectRef": {
    "resource": "pods",
    "namespace": "default",
    "name": "my-pod",
    "subresource": "exec"
  },
  "responseStatus": {
    "code": 101
  },
  "requestReceivedTimestamp": "2026-02-16T14:01:06.056518Z",
  "annotations": {
    "authorization.k8s.io/decision": "allow",
    "authorization.k8s.io/reason": "RBAC: allowed by ClusterRoleBinding...",
    "execmetadata.spo.io/SPO_EXEC_REQUEST_UID": "aec3e0e1-xxxx-xxxx-xxxx-a7c58241f1a9"
}
```

The final field in this example, `SPO_EXEC_REQUEST_UID` is the correlation key.

# Correlation key

You can build a complete audit trail by matching correlation keys across logs. The `requestUID` field in Audit JSON Enricher logs matches the `annotations.execmetadata.spo.io/SPO_EXEC_REQUEST_UID` annotation in the Kubernetes API audit log.

For example, the API audit log can show that `kube:admin` ran a command, and the SPO JSON Enricher log can show the system-level action, such as `touch /tmp/testfile.txt`.

``` text
aec3e0e1-xxxx-xxxx-xxxx-a7c58241f1a9
```

# Correlating with API Server Audit Log

By default, when you use the `kubectl exec` command to access a pod or container, Kubernetes does not pass the user’s authentication details into that session’s environment. This means the Audit JSON log enricher cannot provide audit information for `exec` commands. The `UID` or `GID` shown, maps to the system user. In most cases this would be the root user.

To address this, the Audit JSON log enricher relies on mutating webhooks (`execmetadata.spo.io` and `nodedebuggingpod.spo.io`). The webhook injects the exec `requestUID` as an environment variable into the `exec` session. When the administrator enables audit logging on the API server, the webhooks add the `SPO_EXEC_REQUEST_UID` audit annotation. The API server audit log contains this information. This request ID is also available in the JSON lines produced by the Audit JSON log enricher, specifically within the `requestUID` field.

By default, these webhooks are enabled for all namespaces with the Audit JSON log enricher enabled. To reduce the scope of this webhook you can disable it for certain namespaces.

<div>

<div class="title">

Procedure

</div>

1.  Edit the spod security profile by running the following command:

    ``` terminal
    $ oc edit spod spod -n openshift-security-profiles
    ```

2.  Add `webhookOptions` to the `spec`. Locate the `spec` section and add the following `webhookOptions` block to instruct the webhook to apply to a specific namespace.

    ``` yaml
    spec:
      webhookOptions:
        - name: execmetadata.spo.io # or nodedebuggingpod.spo.io
          namespaceSelector:
          #...add rules
    ```

    After saving your changes, the Operator reconfigures the mutating webhook, allowing request details to be passed into `oc exec` sessions cluster-wide.

</div>

# Use the mutating webhook

Use the mutating webhook so Advanced Audit Logging can correlate cluster users with actions in `oc exec`, `oc rsh`, and `oc debug` sessions.

The mutating webhook injects the `SPO_EXEC_REQUEST_UID` environment variable into your exec request. If a container already defines a variable with that name, the injected value overrides it for the exec session.

When you use `kubectl debug node/<node_name>`, the `nodedebuggingpod.spo.io` webhook injects `SPO_EXEC_REQUEST_UID` into the debug pod.

## The debug pod

This webhook primarily identifies kubectl debug pods by the label `app.kubernetes.io/managed-by: kubectl-debug`, which is added by the kubectl client. Because this label might vary across different Kubernetes client implementations, such as how `oc debug` in OpenShift Container Platform uses `debug.openshift.io/managed-by: oc-debug`, you might need to configure additional `webhookOptions` to ensure the webhook catches all relevant debug pods.

For example, to add oc debug pods, use the following `yaml`:

``` terminal
# ... (rest of your spod configuration)
spec:
  webhookOptions:
    - name: nodedebuggingpodmetada.spo.io
      objectSelector:
        matchLabels: # Use matchLabels for exact matching
          debug.openshift.io/managed-by: "oc-debug"
# ... (other webhook rule details such as rules, clientConfig, etc.)
```

# Disabling Advanced Audit Logging

You can disable advanced audit logging and revert all configurations by deleting the test pod, the `seccompProfile`, the JSON Log Enricher and resetting all `spod` pod options.

<div>

<div class="title">

Procedure

</div>

1.  Delete the test pod with the following command:

    ``` terminal
    oc delete pod my-pod
    ```

2.  Delete the `seccompProfile` using this command:

    ``` terminal
    oc delete seccompprofile profile1 -n openshift-security-profiles
    ```

3.  Disable the JSON Log Enricher and reset all options:

    ``` terminal
    oc patch spod spod -n openshift-security-profiles --type merge -p '{ "spec": { "enableJsonEnricher": false, "jsonEnricherOptions": { "auditLogPath": "", "auditLogMaxSize": 0, "auditLogMaxBackups": 0, "auditLogMaxAge": 0, "auditLogIntervalSeconds": 0 } }}'
    ```

4.  Wait for `spod` pods to restart. Run the following command to check:

    ``` terminal
    oc get pods -n openshift-security-profiles -l name=spod -w
    ```

    Wait until all `spod` pods show `Running`.

5.  Revert the ConfigMap volume patch with the following command:

    ``` terminal
    oc patch configmap security-profiles-operator-profile -n openshift-security-profiles --type merge -p '{"data":{"patch-volume-source.json":""}}'
    ```

6.  Verify that the configuration has been successfully updated:

    ``` terminal
    oc get spod spod -n openshift-security-profiles -o jsonpath='{.spec.enableJsonEnricher}'
    ```

    Expected output:

    ``` terminal
    false
    ```

</div>

# Additional resources

- [About security profiles](spo-understanding.md#spo-about_spo-understanding)

- [Installing the Security Profiles Operator](spo-enabling.md#spo-installing_spo-enabling)

- [Migration procedure](https://access.redhat.com/articles/7130594)

- [Use the log enricher](spo-advanced.md#spo-log-enricher_spo-advanced)

- [Troubleshooting the Security Profiles Operator](spo-troubleshooting.md#spo-inspecting-seccomp-profiles_spo-troubleshooting)

- [Uninstalling SPO](spo-uninstalling.md#spo-uninstalling)
