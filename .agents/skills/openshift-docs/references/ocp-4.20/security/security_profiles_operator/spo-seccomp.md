<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Create and manage seccomp profiles and bind them to workloads.

> [!IMPORTANT]
> The Security Profiles Operator supports only Red Hat Enterprise Linux CoreOS (RHCOS) worker nodes. Red Hat Enterprise Linux (RHEL) nodes are not supported.

# Creating seccomp profiles

Use the `SeccompProfile` object to create seccomp profiles.

`SeccompProfile` objects can restrict syscalls within a container, limiting the access of your application.

<div>

<div class="title">

Procedure

</div>

1.  Create a project by running the following command:

    ``` terminal
    $ oc new-project my-namespace
    ```

2.  Create the `SeccompProfile` object:

    ``` yaml
    apiVersion: security-profiles-operator.x-k8s.io/v1beta1
    kind: SeccompProfile
    metadata:
      name: profile1
    spec:
      defaultAction: SCMP_ACT_LOG
    ```

    The seccomp profile will be saved in `/var/lib/kubelet/seccomp/operator/<namespace>/<name>.json`.

    An `init` container creates the root directory of the Security Profiles Operator to run the Operator without `root` group or user ID privileges. A symbolic link is created from the rootless profile storage `/var/lib/openshift-security-profiles` to the default `seccomp` root path inside of the kubelet root `/var/lib/kubelet/seccomp/operator`.

</div>

# Applying seccomp profiles to a pod

Create a pod to apply one of the created profiles.

<div>

<div class="title">

Procedure

</div>

1.  Create a pod object that defines a `securityContext`:

    ``` yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: test-pod
    spec:
      securityContext:
        runAsNonRoot: true
        seccompProfile:
          type: Localhost
          localhostProfile: operator/profile1.json
      containers:
        - name: test-container
          image: quay.io/security-profiles-operator/test-nginx-unprivileged:1.21
          securityContext:
            allowPrivilegeEscalation: false
            capabilities:
              drop: [ALL]
    ```

2.  View the profile path of the `seccompProfile.localhostProfile` attribute by running the following command:

    ``` terminal
    $ oc get seccompprofile profile1 --output wide
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME       STATUS     AGE   SECCOMPPROFILE.LOCALHOSTPROFILE
    profile1   Installed  14s   operator/profile1.json
    ```

    </div>

3.  View the path to the localhost profile by running the following command:

    ``` terminal
    $ oc get sp profile1 --output=jsonpath='{.status.localhostProfile}'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    operator/profile1.json
    ```

    </div>

4.  Apply the `localhostProfile` output to the patch file:

    ``` yaml
    spec:
      template:
        spec:
          securityContext:
            seccompProfile:
              type: Localhost
              localhostProfile: operator/profile1.json
    ```

5.  Apply the profile to any other workload, such as a `Deployment` object, by running the following command:

    ``` terminal
    $ oc -n my-namespace patch deployment myapp --patch-file patch.yaml --type=merge
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    deployment.apps/myapp patched
    ```

    </div>

</div>

<div>

<div class="title">

Verification

</div>

- Confirm the profile was applied correctly by running the following command:

  ``` terminal
  $ oc -n my-namespace get deployment myapp --output=jsonpath='{.spec.template.spec.securityContext}' | jq .
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` json
  {
    "seccompProfile": {
      "localhostProfile": "operator/profile1.json",
      "type": "localhost"
    }
  }
  ```

  </div>

</div>

## Binding workloads to profiles with ProfileBindings

You can use the `ProfileBinding` resource to bind a security profile to the `SecurityContext` of a container.

<div>

<div class="title">

Procedure

</div>

1.  To bind a pod that uses a `quay.io/security-profiles-operator/test-nginx-unprivileged:1.21` image to the example `SeccompProfile` profile, create a `ProfileBinding` object in the same namespace with the pod and the `SeccompProfile` objects:

    ``` yaml
    apiVersion: security-profiles-operator.x-k8s.io/v1alpha1
    kind: ProfileBinding
    metadata:
      namespace: my-namespace
      name: nginx-binding
    spec:
      profileRef:
        kind: SeccompProfile
        name: profile
      image: quay.io/security-profiles-operator/test-nginx-unprivileged:1.21
    ```

    where:

    `spec.profileRef.kind`
    Specifies the kind of the profile.

    `spec.profileRef.name`
    Specifies the name of the profile.

    `spec.image`
    Allows you to enable a default security profile by using a wildcard in the image attribute: `image: "*"`

    > [!IMPORTANT]
    > Using the `image: "*"` wildcard attribute binds all new pods with a default security profile in a given namespace.

2.  Label the namespace with `enable-binding=true` by running the following command:

    ``` terminal
    $ oc label ns my-namespace spo.x-k8s.io/enable-binding=true
    ```

3.  Define a pod named `test-pod.yaml`:

    ``` yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: test-pod
    spec:
      containers:
      - name: test-container
        image: quay.io/security-profiles-operator/test-nginx-unprivileged:1.21
    ```

4.  Create the pod:

    ``` terminal
    $ oc create -f test-pod.yaml
    ```

    > [!NOTE]
    > If the pod already exists, you must re-create the pod for the binding to work properly.

</div>

<div>

<div class="title">

Verification

</div>

- Confirm the pod inherits the `ProfileBinding` by running the following command:

  ``` terminal
  $ oc get pod test-pod -o jsonpath='{.spec.containers[*].securityContext.seccompProfile}'
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  {"localhostProfile":"operator/profile.json","type":"Localhost"}
  ```

  </div>

</div>

# Recording profiles from workloads

The Security Profiles Operator can record system calls with `ProfileRecording` objects, making it easier to create baseline profiles for applications.

When using the log enricher for recording seccomp profiles, verify the log enricher feature is enabled. See *Additional resources* for more information.

> [!NOTE]
> A container with `privileged: true` security context restraints prevents log-based recording. Privileged containers are not subject to seccomp policies, and log-based recording makes use of a special seccomp profile to record events.

<div>

<div class="title">

Procedure

</div>

1.  Create a project by running the following command:

    ``` terminal
    $ oc new-project my-namespace
    ```

2.  Label the namespace with `enable-recording=true` by running the following command:

    ``` terminal
    $ oc label ns my-namespace spo.x-k8s.io/enable-recording=true
    ```

3.  Create a `ProfileRecording` object containing a `recorder: logs` variable:

    ``` yaml
    apiVersion: security-profiles-operator.x-k8s.io/v1alpha1
    kind: ProfileRecording
    metadata:
      namespace: my-namespace
      name: test-recording
    spec:
      kind: SeccompProfile
      recorder: logs
      podSelector:
        matchLabels:
          app: my-app
    ```

4.  Create a workload to record:

    ``` yaml
    apiVersion: v1
    kind: Pod
    metadata:
      namespace: my-namespace
      name: my-pod
      labels:
        app: my-app
    spec:
      securityContext:
        runAsNonRoot: true
        seccompProfile:
          type: RuntimeDefault
      containers:
        - name: nginx
          image: quay.io/security-profiles-operator/test-nginx-unprivileged:1.21
          ports:
            - containerPort: 8080
          securityContext:
            allowPrivilegeEscalation: false
            capabilities:
              drop: [ALL]
        - name: redis
          image: quay.io/security-profiles-operator/redis:6.2.1
          securityContext:
            allowPrivilegeEscalation: false
            capabilities:
              drop: [ALL]
    ```

5.  Confirm the pod is in a `Running` state by entering the following command:

    ``` terminal
    $ oc -n my-namespace get pods
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME     READY   STATUS    RESTARTS   AGE
    my-pod   2/2     Running   0          18s
    ```

    </div>

6.  Confirm the enricher indicates that it receives audit logs for those containers:

    ``` terminal
    $ oc -n openshift-security-profiles logs --since=1m --selector name=spod -c log-enricher
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    I0523 14:19:08.747313  430694 enricher.go:445] log-enricher "msg"="audit" "container"="redis" "executable"="/usr/local/bin/redis-server" "namespace"="my-namespace" "node"="xiyuan-23-5g2q9-worker-eastus2-6rpgf" "pid"=656802 "pod"="my-pod" "syscallID"=0 "syscallName"="read" "timestamp"="1684851548.745:207179" "type"="seccomp"
    ```

    </div>

</div>

<div>

<div class="title">

Verification

</div>

1.  Remove the pod:

    ``` terminal
    $ oc -n my-namespace delete pod my-pod
    ```

2.  Confirm the Security Profiles Operator reconciles the two seccomp profiles:

    ``` terminal
    $ oc get seccompprofiles -lspo.x-k8s.io/recording-id=test-recording
    ```

    <div class="formalpara">

    <div class="title">

    Example output for seccompprofile

    </div>

    ``` terminal
    NAME                   STATUS      AGE
    test-recording-nginx   Installed   2m48s
    test-recording-redis   Installed   2m48s
    ```

    </div>

</div>

## Merging per-container profile instances

By default, each container instance records into a separate profile. The Security Profiles Operator can merge the per-container profiles into a single profile. Merging profiles is useful when deploying applications using `ReplicaSet` or `Deployment` objects.

<div>

<div class="title">

Procedure

</div>

1.  Edit a `ProfileRecording` object to include a `mergeStrategy: containers` variable:

    ``` yaml
    apiVersion: security-profiles-operator.x-k8s.io/v1alpha1
    kind: ProfileRecording
    metadata:
      # The name of the Recording is the same as the resulting SeccompProfile CRD
      # after reconciliation.
      name: test-recording
      namespace: my-namespace
    spec:
      kind: SeccompProfile
      recorder: logs
      mergeStrategy: containers
      podSelector:
        matchLabels:
          app: sp-record
    ```

2.  Label the namespace by running the following command:

    ``` terminal
    $ oc label ns my-namespace security.openshift.io/scc.podSecurityLabelSync=false pod-security.kubernetes.io/enforce=privileged pod-security.kubernetes.io/audit=privileged pod-security.kubernetes.io/warn=privileged --overwrite=true
    ```

3.  Create the workload with the following YAML:

    ``` yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: nginx-deploy
      namespace: my-namespace
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: sp-record
      template:
        metadata:
          labels:
            app: sp-record
        spec:
          serviceAccountName: spo-record-sa
          containers:
          - name: nginx-record
            image: quay.io/security-profiles-operator/test-nginx-unprivileged:1.21
            ports:
            - containerPort: 8080
    ```

4.  To record the individual profiles, delete the deployment by running the following command:

    ``` terminal
    $ oc delete deployment nginx-deploy -n my-namespace
    ```

5.  To merge the profiles, delete the profile recording by running the following command:

    ``` terminal
    $ oc delete profilerecording test-recording -n my-namespace
    ```

6.  To start the merge operation and generate the results profile, run the following command:

    ``` terminal
    $ oc get seccompprofiles -lspo.x-k8s.io/recording-id=test-recording -n my-namespace
    ```

    <div class="formalpara">

    <div class="title">

    Example output for seccompprofiles

    </div>

    ``` terminal
    NAME                          STATUS       AGE
    test-recording-nginx-record   Installed    55s
    ```

    </div>

7.  To view the permissions used by any of the containers, run the following command:

    ``` terminal
    $ oc get seccompprofiles test-recording-nginx-record -o yaml
    ```

</div>

# Additional resources

- [Managing security context constraints](../../authentication/managing-security-context-constraints.md#managing-pod-security-policies)

- [Managing SCCs in OpenShift](https://cloud.redhat.com/blog/managing-sccs-in-openshift)

- [Using the log enricher](spo-advanced.md#spo-log-enricher_spo-advanced)

- [About security profiles](spo-understanding.md#spo-about_spo-understanding)
