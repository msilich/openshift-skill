<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

An OpenShift Container Platform container or a pod runs a single application that performs one or more well-defined tasks. The application usually requires only a small subset of the underlying operating system kernel APIs. Secure computing mode, seccomp, is a Linux kernel feature that can be used to limit the process running in a container to only using a subset of the available system calls.

The `restricted-v2` SCC applies to all newly created pods in 4.17. The default seccomp profile `runtime/default` is applied to these pods.

Seccomp profiles are stored as JSON files on the disk.

> [!IMPORTANT]
> Seccomp profiles cannot be applied to privileged containers.

# Verifying the default seccomp profile applied to a pod

OpenShift Container Platform ships with a default seccomp profile that is referenced as `runtime/default`. In 4.17, newly created pods have the Security Context Constraint (SCC) set to `restricted-v2` and the default seccomp profile applies to the pod.

<div>

<div class="title">

Procedure

</div>

1.  You can verify the Security Context Constraint (SCC) and the default seccomp profile set on a pod by running the following commands:

    1.  Verify what pods are running in the namespace:

        ``` terminal
        $ oc get pods -n <namespace>
        ```

        For example, to verify what pods are running in the `workshop` namespace run the following:

        ``` terminal
        $ oc get pods -n workshop
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME                READY   STATUS      RESTARTS   AGE
        parksmap-1-4xkwf    1/1     Running     0          2m17s
        parksmap-1-deploy   0/1     Completed   0          2m22s
        ```

        </div>

    2.  Inspect the pods:

        ``` terminal
        $ oc get pod parksmap-1-4xkwf -n workshop -o yaml
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        apiVersion: v1
        kind: Pod
        metadata:
          annotations:
            k8s.v1.cni.cncf.io/network-status: |-
              [{
                  "name": "ovn-kubernetes",
                  "interface": "eth0",
                  "ips": [
                      "10.131.0.18"
                  ],
                  "default": true,
                  "dns": {}
              }]
            k8s.v1.cni.cncf.io/network-status: |-
              [{
                  "name": "ovn-kubernetes",
                  "interface": "eth0",
                  "ips": [
                      "10.131.0.18"
                  ],
                  "default": true,
                  "dns": {}
              }]
            openshift.io/deployment-config.latest-version: "1"
            openshift.io/deployment-config.name: parksmap
            openshift.io/deployment.name: parksmap-1
            openshift.io/generated-by: OpenShiftWebConsole
            openshift.io/scc: restricted-v2
            seccomp.security.alpha.kubernetes.io/pod: runtime/default
        ```

        </div>

        - The `restricted-v2` SCC is added by default if your workload does not have access to a different SCC.

        - Newly created pods in 4.17 will have the seccomp profile configured to `runtime/default` as mandated by the SCC.

</div>

## Upgraded cluster

In clusters upgraded to 4.17 all authenticated users have access to the `restricted` and `restricted-v2` SCC.

A workload admitted by the SCC `restricted` for example, on a OpenShift Container Platform v4.10 cluster when upgraded may get admitted by `restricted-v2`. This is because `restricted-v2` is the more restrictive SCC between `restricted` and `restricted-v2`.

> [!NOTE]
> The workload must be able to run with `retricted-v2`.

Conversely with a workload that requires `privilegeEscalation: true` this workload will continue to have the `restricted` SCC available for any authenticated user. This is because `restricted-v2` does not allow `privilegeEscalation`.

## Newly installed cluster

For newly installed OpenShift Container Platform 4.11 or later clusters, the `restricted-v2` replaces the `restricted` SCC as an SCC that is available to be used by any authenticated user. A workload with `privilegeEscalation: true`, is not admitted into the cluster since `restricted-v2` is the only SCC available for authenticated users by default.

The feature `privilegeEscalation` is allowed by `restricted` but not by `restricted-v2`. More features are denied by `restricted-v2` than were allowed by `restricted` SCC.

A workload with `privilegeEscalation: true` may be admitted into a newly installed OpenShift Container Platform 4.11 or later cluster. To give access to the `restricted` SCC to the ServiceAccount running the workload (or any other SCC that can admit this workload) using a RoleBinding run the following command:

``` terminal
$ oc -n <workload-namespace> adm policy add-scc-to-user <scc-name> -z <serviceaccount_name>
```

In OpenShift Container Platform 4.17 the ability to add the pod annotations `seccomp.security.alpha.kubernetes.io/pod: runtime/default` and `container.seccomp.security.alpha.kubernetes.io/<container_name>: runtime/default` is deprecated.

# Configuring a custom seccomp profile

You can configure a custom seccomp profile, which allows you to update the filters based on the application requirements. This allows cluster administrators to have greater control over the security of workloads running in OpenShift Container Platform.

Seccomp security profiles list the system calls (syscalls) a process can make. Permissions are broader than SELinux, which restrict operations, such as `write`, system-wide.

## Creating seccomp profiles

You can use the `MachineConfig` object to create profiles.

Seccomp can restrict system calls (syscalls) within a container, limiting the access of your application.

<div>

<div class="title">

Prerequisites

</div>

- You have cluster admin permissions.

- You have created a custom security context constraints (SCC). For more information, see *Additional resources*.

</div>

<div>

<div class="title">

Procedure

</div>

- Create the `MachineConfig` object:

  ``` yaml
  apiVersion: machineconfiguration.openshift.io/v1
  kind: MachineConfig
  metadata:
    labels:
      machineconfiguration.openshift.io/role: worker
    name: custom-seccomp
  spec:
    config:
      ignition:
        version: 3.2.0
      storage:
        files:
        - contents:
            source: data:text/plain;charset=utf-8;base64,<hash>
          filesystem: root
          mode: 0644
          path: /var/lib/kubelet/seccomp/seccomp-nostat.json
  ```

</div>

## Setting up the custom seccomp profile

<div>

<div class="title">

Prerequisite

</div>

- You have cluster administrator permissions.

- You have created a custom security context constraints (SCC). For more information, see "Additional resources".

- You have created a custom seccomp profile.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Upload your custom seccomp profile to `/var/lib/kubelet/seccomp/<custom-name>.json` by using the Machine Config. See "Additional resources" for detailed steps.

2.  Update the custom SCC by providing reference to the created custom seccomp profile:

    ``` yaml
    seccompProfiles:
    - localhost/<custom-name>.json
    ```

    - Provide the name of your custom seccomp profile.

</div>

## Applying the custom seccomp profile to the workload

<div>

<div class="title">

Prerequisite

</div>

- The cluster administrator has set up the custom seccomp profile. For more details, see "Setting up the custom seccomp profile".

</div>

<div>

<div class="title">

Procedure

</div>

- Apply the seccomp profile to the workload by setting the `securityContext.seccompProfile.type` field as following:

  <div class="formalpara">

  <div class="title">

  Example

  </div>

  ``` yaml
  spec:
    securityContext:
      seccompProfile:
        type: Localhost
        localhostProfile: <custom-name>.json
  ```

  </div>

  - Provide the name of your custom seccomp profile.

    Alternatively, you can use the pod annotations `seccomp.security.alpha.kubernetes.io/pod: localhost/<custom-name>.json`. However, this method is deprecated in OpenShift Container Platform 4.17.

</div>

During deployment, the admission controller validates the following:

- The annotations against the current SCCs allowed by the user role.

- The SCC, which includes the seccomp profile, is allowed for the pod.

If the SCC is allowed for the pod, the kubelet runs the pod with the specified seccomp profile.

> [!IMPORTANT]
> Ensure that the seccomp profile is deployed to all worker nodes.

> [!NOTE]
> The custom SCC must have the appropriate priority to be automatically assigned to the pod or meet other conditions required by the pod, such as allowing CAP_NET_ADMIN.

# Additional resources

- [Managing security context constraints](../authentication/managing-security-context-constraints.md)

- [Machine Config Overview](../machine_configuration/index.md#machine-config-overview)
