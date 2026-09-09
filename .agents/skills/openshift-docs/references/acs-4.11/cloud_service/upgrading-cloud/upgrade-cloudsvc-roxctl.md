<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can upgrade your secured clusters in RHACS Cloud Service by using the `roxctl` CLI.

> [!IMPORTANT]
> You need to manually upgrade secured clusters only if you used the `roxctl` CLI to install the secured clusters.

<a id="upgrade-roxctl-cli_upgrade-cloudsvc-roxctl"></a>

# Upgrading the roxctl CLI

To upgrade the `roxctl` CLI to the latest version, you must uninstall your current version of the `roxctl` CLI and then install the latest version of the `roxctl` CLI.

<a id="uninstalling-cli-on-linux_upgrade-cloudsvc-roxctl"></a>

## Uninstalling the roxctl CLI

You can uninstall the `roxctl` CLI binary on Linux by using the following procedure.

<div>

<div class="title">

Procedure

</div>

- Find and delete the `roxctl` binary:

  ``` terminal
  $ ROXPATH=$(which roxctl) && rm -f $ROXPATH
  ```

  > [!NOTE]
  > Depending on your environment, you might need administrator rights to delete the `roxctl` binary.

</div>

<a id="installing-cli-on-linux_upgrade-cloudsvc-roxctl"></a>

## Installing the roxctl CLI on Linux

You can install the `roxctl` CLI binary on Linux by using the following procedure.

> [!NOTE]
> `roxctl` CLI for Linux is available for `amd64`, `arm64`, `ppc64le`, and `s390x` architectures.

<div>

<div class="title">

Procedure

</div>

1.  Find the `roxctl` architecture for the target operating system:

    ``` terminal
    $ arch="$(uname -m | sed "s/x86_64//")"; arch="${arch:+-$arch}"
    ```

2.  Download the `roxctl` CLI:

    ``` terminal
    $ curl -L -f -o roxctl "https://mirror.openshift.com/pub/rhacs/assets/4.11.3/bin/Linux/roxctl${arch}"
    ```

3.  Make the `roxctl` binary executable:

    ``` terminal
    $ chmod +x roxctl
    ```

4.  Place the `roxctl` binary in a directory that is on your `PATH`:

    To check your `PATH`, run the following command:

    ``` terminal
    $ echo $PATH
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify the `roxctl` version you have installed:

  ``` terminal
  $ roxctl version
  ```

</div>

<a id="installing-cli-on-macos_upgrade-cloudsvc-roxctl"></a>

## Installing the roxctl CLI on macOS

You can install the `roxctl` CLI binary on macOS by using the following procedure.

> [!NOTE]
> `roxctl` CLI for macOS is available for `amd64` and `arm64` architectures.

<div>

<div class="title">

Procedure

</div>

1.  Find the `roxctl` architecture for the target operating system:

    ``` terminal
    $ arch="$(uname -m | sed "s/x86_64//")"; arch="${arch:+-$arch}"
    ```

2.  Download the `roxctl` CLI:

    ``` terminal
    $ curl -L -f -o roxctl "https://mirror.openshift.com/pub/rhacs/assets/4.11.3/bin/Darwin/roxctl${arch}"
    ```

3.  Remove all extended attributes from the binary:

    ``` terminal
    $ xattr -c roxctl
    ```

4.  Make the `roxctl` binary executable:

    ``` terminal
    $ chmod +x roxctl
    ```

5.  Place the `roxctl` binary in a directory that is on your `PATH`:

    To check your `PATH`, run the following command:

    ``` terminal
    $ echo $PATH
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify the `roxctl` version you have installed:

  ``` terminal
  $ roxctl version
  ```

</div>

<a id="installing-cli-on-windows_upgrade-cloudsvc-roxctl"></a>

## Installing the roxctl CLI on Windows

You can install the `roxctl` CLI binary on Windows by using the following procedure.

> [!NOTE]
> `roxctl` CLI for Windows is available for the `amd64` architecture.

<div>

<div class="title">

Procedure

</div>

- Download the `roxctl` CLI:

  ``` terminal
  $ curl -f -O https://mirror.openshift.com/pub/rhacs/assets/4.11.3/bin/Windows/roxctl.exe
  ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify the `roxctl` version you have installed:

  ``` terminal
  $ roxctl version
  ```

</div>

<a id="upgrade-secured-clusters-cloud_upgrade-cloudsvc-roxctl"></a>

# Upgrading all secured clusters manually

To complete manual upgrades of each secured cluster that runs Sensor, Collector, and Admission controller, follow these instructions.

> [!IMPORTANT]
> To ensure optimal functionality, use the same RHACS version for your secured clusters that RHACS Cloud Service is running. If you are using automatic upgrades, update all your secured clusters by using automatic upgrades. If you are not using automatic upgrades, complete the instructions in this section on all secured clusters.

<a id="update-other-images_upgrade-cloudsvc-roxctl"></a>

## Updating other images

You must update the sensor, collector and compliance images on each secured cluster when not using automatic upgrades.

> [!NOTE]
> If you are using Kubernetes, use `kubectl` instead of `oc` for the commands listed in this procedure.

<div>

<div class="title">

Procedure

</div>

1.  Update the Sensor image:

    ``` terminal
    $ oc -n stackrox set image deploy/sensor sensor=registry.redhat.io/advanced-cluster-security/rhacs-main-rhel9:4.11.3
    ```

2.  Update the Compliance image:

    ``` terminal
    $ oc -n stackrox set image ds/collector compliance=registry.redhat.io/advanced-cluster-security/rhacs-main-rhel9:4.11.3
    ```

3.  Update the Collector image:

    ``` terminal
    $ oc -n stackrox set image ds/collector collector=registry.redhat.io/advanced-cluster-security/rhacs-collector-rhel9:4.11.3
    ```

4.  Update the admission control image:

    ``` terminal
    $ oc -n stackrox set image deploy/admission-control admission-control=registry.redhat.io/advanced-cluster-security/rhacs-main-rhel9:4.11.3
    ```

    > [!IMPORTANT]
    > If you have installed RHACS on Red Hat OpenShift by using the `roxctl` CLI, you need to migrate the security context constraints (SCCs).

</div>

<div>

<div class="title">

Additional resources

</div>

- [Authenticating by using the roxctl CLI](../../cli/using-the-roxctl-cli.md#authenticating-by-using-the-roxctl-cli_using-roxctl-cli)

</div>

<a id="migrating-sccs-during-the-manual-upgrade_upgrade-cloudsvc-roxctl"></a>

## Migrating security context constraints during the manual upgrade

By migrating the security context constraints (SCCs) during the manual upgrade by using `roxctl` CLI, you can seamlessly migrate the Red Hat Advanced Cluster Security for Kubernetes (RHACS) services to use the Red Hat OpenShift SCCs, ensuring compatibility and optimal security configurations across Central and all secured clusters.

<div>

<div class="title">

Procedure

</div>

1.  List all of the RHACS services running on all secured clusters:

    ``` terminal
    $ oc -n stackrox describe pods | grep 'openshift.io/scc\|^Name:'
    ```

    The following is an example output:

    ``` text
    Name:      admission-control-6f4dcc6b4c-2phwd
               openshift.io/scc: stackrox-admission-control
    #...
    Name:      central-575487bfcb-sjdx8
               openshift.io/scc: stackrox-central
    Name:      central-db-7c7885bb-6bgbd
               openshift.io/scc: stackrox-central-db
    Name:      collector-56nkr
               openshift.io/scc: stackrox-collector
    #...
    Name:      scanner-68fc55b599-f2wm6
               openshift.io/scc: stackrox-scanner
    Name:      scanner-68fc55b599-fztlh
    #...
    Name:      sensor-84545f86b7-xgdwf
               openshift.io/scc: stackrox-sensor
    #...
    ```

    In this example, you can see that each pod has its own custom SCC, which the `openshift.io/scc` field specifies.

2.  Add the required roles and role bindings to use the Red Hat OpenShift SCCs instead of the RHACS custom SCCs.

3.  To add the required roles and role bindings to use the Red Hat OpenShift SCCs for all secured clusters, complete the following steps:

    1.  Create a file named `upgrade-scs.yaml` that defines the role and role binding resources by using the following content:

        ``` yaml
        apiVersion: rbac.authorization.k8s.io/v1
        kind: Role  #
        metadata:
          annotations:
             email: support@stackrox.com
             owner: stackrox
          labels:
             app.kubernetes.io/component: collector
             app.kubernetes.io/instance: stackrox-secured-cluster-services
             app.kubernetes.io/name: stackrox
             app.kubernetes.io/part-of: stackrox-secured-cluster-services
             app.kubernetes.io/version: 4.4.0
             auto-upgrade.stackrox.io/component: sensor
          name: use-privileged-scc  #
          namespace: stackrox #
        rules:  #
        - apiGroups:
          - security.openshift.io
          resourceNames:
          - privileged
          resources:
          - securitycontextconstraints
          verbs:
          - use
        - - -
        apiVersion: rbac.authorization.k8s.io/v1
        kind: RoleBinding #
        metadata:
          annotations:
             email: support@stackrox.com
             owner: stackrox
          labels:
             app.kubernetes.io/component: collector
             app.kubernetes.io/instance: stackrox-secured-cluster-services
             app.kubernetes.io/name: stackrox
             app.kubernetes.io/part-of: stackrox-secured-cluster-services
             app.kubernetes.io/version: 4.4.0
             auto-upgrade.stackrox.io/component: sensor
          name: collector-use-scc #
          namespace: stackrox
        roleRef: #
          apiGroup: rbac.authorization.k8s.io
          kind: Role
          name: use-privileged-scc
        subjects: #
        - kind: ServiceAccount
          name: collector
          namespace: stackrox
        - - -
        ```

        where:

        `kind: Role`  
        Specifies the type of Kubernetes resource, in this example, `Role`.

        `metadata.name: <rolename>`  
        Specifies the name of the role resource.

        `metadata.namespace`  
        Specifies the namespace for the role.

        `Rules`  
        Specifies the permissions granted by the role resource.

        `kind: RoleBinding`  
        Specifies the type of Kubernetes resource, in this example, `RoleBinding`.

        `metadata.name: <rolebindingname>`  
        Specifies the name of the role binding resource.

        `metadata.roleRef`  
        Specifies the role to bind in the same namespace.

        `metadata.subjects`  
        Specifies the subjects to bind to the role.

    2.  Create the role and role binding resources specified in the `upgrade-scs.yaml` file by running the following command:

        ``` terminal
        $ oc -n stackrox create -f ./update-scs.yaml
        ```

        > [!IMPORTANT]
        > You must run this command on each secured cluster to create the role and role bindings specified in the `upgrade-scs.yaml` file.

4.  Delete the SCCs that are specific to RHACS:

    1.  To delete the SCCs that are specific to all secured clusters, run the following command:

        ``` terminal
        $ oc delete scc/stackrox-admission-control scc/stackrox-collector scc/stackrox-sensor
        ```

        > [!IMPORTANT]
        > You must run this command on each secured cluster to delete the SCCs that are specific to each secured cluster.

</div>

<div>

<div class="title">

Verification

</div>

- Ensure that all the pods are using the correct SCCs by running the following command:

  ``` terminal
  $ oc -n stackrox describe pods | grep 'openshift.io/scc\|^Name:'
  ```

  Compare the output with the following table:

  | Component | Earlier custom SCC | New Red Hat OpenShift 4 SCC |
  |----|----|----|
  | Central | `stackrox-central` | `nonroot-v2` |
  | Central-db | `stackrox-central-db` | `nonroot-v2` |
  | Scanner | `stackrox-scanner` | `nonroot-v2` |
  | Scanner-db | `stackrox-scanner` | `nonroot-v2` |
  | Admission Controller | `stackrox-admission-control` | `restricted-v2` |
  | Collector | `stackrox-collector` | `privileged` |
  | Sensor | `stackrox-sensor` | `restricted-v2` |

</div>

<a id="verify-secured-cluster-upgrade_upgrade-cloudsvc-roxctl"></a>

## Verifying secured cluster upgrade

After you have upgraded secured clusters, verify that the updated pods are working.

> [!NOTE]
> If you use Kubernetes, enter `kubectl` instead of `oc`.

<div>

<div class="title">

Procedure

</div>

- Check that the new pods have deployed:

  ``` terminal
  $ oc get deploy,ds -n stackrox -o wide
  ```

  ``` terminal
  $ oc get pod -n stackrox --watch
  ```

</div>

<a id="rhcos-enable-node-scan_upgrade-cloudsvc-roxctl"></a>

# Enabling RHCOS node scanning with the StackRox Scanner

If you use OpenShift Container Platform, you can enable scanning of Red Hat Enterprise Linux CoreOS (RHCOS) nodes for vulnerabilities by using Red Hat Advanced Cluster Security for Kubernetes (RHACS).

> [!NOTE]
> Use Scanner V4 for full functionality when scanning nodes. For instructions on changing to Scanner V4 if you are using the StackRox scanner, see "Enabling Scanner V4".

<div>

<div class="title">

Prerequisites

</div>

- For scanning RHCOS node hosts of the secured cluster, you must have installed Secured Cluster services on OpenShift Container Platform 4.12 or later. For information about supported platforms and architecture, see the "Red Hat Advanced Cluster Security for Kubernetes Support Matrix". For life cycle support information for RHACS, see the "Red Hat Advanced Cluster Security for Kubernetes Support Policy".

- This procedure describes how to enable node scanning for the first time. If you are reconfiguring Red Hat Advanced Cluster Security for Kubernetes to use the StackRox Scanner instead of Scanner V4, follow the procedure in "Restoring RHCOS node scanning with the StackRox Scanner".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Run one of the following commands to update the compliance container.

    - For a default compliance container with metrics disabled, run the following command:

      ``` terminal
      $ oc -n stackrox patch daemonset/collector -p '{"spec":{"template":{"spec":{"containers":[{"name":"compliance","env":[{"name":"ROX_METRICS_PORT","value":"disabled"},{"name":"ROX_NODE_SCANNING_ENDPOINT","value":"127.0.0.1:8444"},{"name":"ROX_NODE_SCANNING_INTERVAL","value":"4h"},{"name":"ROX_NODE_SCANNING_INTERVAL_DEVIATION","value":"24m"},{"name":"ROX_NODE_SCANNING_MAX_INITIAL_WAIT","value":"5m"},{"name":"ROX_RHCOS_NODE_SCANNING","value":"true"},{"name":"ROX_CALL_NODE_INVENTORY_ENABLED","value":"true"}]}]}}}}'
      ```

    - For a compliance container with Prometheus metrics enabled, run the following command:

      ``` terminal
      $ oc -n stackrox patch daemonset/collector -p '{"spec":{"template":{"spec":{"containers":[{"name":"compliance","env":[{"name":"ROX_METRICS_PORT","value":":9091"},{"name":"ROX_NODE_SCANNING_ENDPOINT","value":"127.0.0.1:8444"},{"name":"ROX_NODE_SCANNING_INTERVAL","value":"4h"},{"name":"ROX_NODE_SCANNING_INTERVAL_DEVIATION","value":"24m"},{"name":"ROX_NODE_SCANNING_MAX_INITIAL_WAIT","value":"5m"},{"name":"ROX_RHCOS_NODE_SCANNING","value":"true"},{"name":"ROX_CALL_NODE_INVENTORY_ENABLED","value":"true"}]}]}}}}'
      ```

2.  Update the Collector DaemonSet (DS) by taking the following steps:

    1.  Add new volume mounts to Collector DS by running the following command:

        ``` terminal
        $ oc -n stackrox patch daemonset/collector -p '{"spec":{"template":{"spec":{"volumes":[{"name":"tmp-volume","emptyDir":{}},{"name":"cache-volume","emptyDir":{"sizeLimit":"200Mi"}}]}}}}'
        ```

    2.  Add the new `NodeScanner` container by running the following command:

        ``` terminal
        $ oc -n stackrox patch daemonset/collector -p '{"spec":{"template":{"spec":{"containers":[{"command":["/scanner","--nodeinventory","--config=",""],"env":[{"name":"ROX_NODE_NAME","valueFrom":{"fieldRef":{"apiVersion":"v1","fieldPath":"spec.nodeName"}}},{"name":"ROX_CLAIR_V4_SCANNING","value":"true"},{"name":"ROX_COMPLIANCE_OPERATOR_INTEGRATION","value":"true"},{"name":"ROX_CSV_EXPORT","value":"false"},{"name":"ROX_DECLARATIVE_CONFIGURATION","value":"false"},{"name":"ROX_INTEGRATIONS_AS_CONFIG","value":"false"},{"name":"ROX_NETPOL_FIELDS","value":"true"},{"name":"ROX_NETWORK_DETECTION_BASELINE_SIMULATION","value":"true"},{"name":"ROX_NETWORK_GRAPH_PATTERNFLY","value":"true"},{"name":"ROX_NODE_SCANNING_CACHE_TIME","value":"3h36m"},{"name":"ROX_NODE_SCANNING_INITIAL_BACKOFF","value":"30s"},{"name":"ROX_NODE_SCANNING_MAX_BACKOFF","value":"5m"},{"name":"ROX_PROCESSES_LISTENING_ON_PORT","value":"false"},{"name":"ROX_QUAY_ROBOT_ACCOUNTS","value":"true"},{"name":"ROX_ROXCTL_NETPOL_GENERATE","value":"true"},{"name":"ROX_SOURCED_AUTOGENERATED_INTEGRATIONS","value":"false"},{"name":"ROX_SYSLOG_EXTRA_FIELDS","value":"true"},{"name":"ROX_SYSTEM_HEALTH_PF","value":"false"},{"name":"ROX_VULN_MGMT_WORKLOAD_CVES","value":"false"}],"image":"registry.redhat.io/advanced-cluster-security/rhacs-scanner-slim-rhel9:4.11.3","imagePullPolicy":"IfNotPresent","name":"node-inventory","ports":[{"containerPort":8444,"name":"grpc","protocol":"TCP"}],"volumeMounts":[{"mountPath":"/host","name":"host-root-ro","readOnly":true},{"mountPath":"/tmp/","name":"tmp-volume"},{"mountPath":"/cache","name":"cache-volume"}]}]}}}}'
        ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Red Hat Advanced Cluster Security for Kubernetes Support Matrix](https://access.redhat.com/articles/7045053)

- [Red Hat Advanced Cluster Security for Kubernetes Support Policy](https://access.redhat.com/support/policy/updates/rhacs)

- [Scanning RHCOS node hosts](../../operating/manage-vulnerabilities/scan-rhcos-node-host.md)

- [Enabling Scanner V4](../../operating/examine-images-for-vulnerabilities.md#scannerv4-enabling_examine-images-for-vulnerabilities)

</div>
