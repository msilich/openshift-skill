<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can upgrade to the latest version of Red Hat Advanced Cluster Security for Kubernetes (RHACS) from a supported older version.

> [!IMPORTANT]
> In RHACS 4.11, all container image names changed from the `-rhel8` suffix to `-rhel9` as part of the migration to UBI 9 Minimal base images. For example, `rhacs-main-rhel8` is now `rhacs-main-rhel9`.
>
> If you use image mirrors, allowlists, or firewall rules that reference specific RHACS image names, you must update them to use the new `-rhel9` names before upgrading. For the complete list of current image names, see [Image versions](../configuration/enable-offline-mode.md#image-versions_enable-offline-mode).

To upgrade RHACS to the latest version, perform the following steps:

1.  Back up the Central database.

2.  Upgrade the `roxctl` CLI.

3.  Upgrade the Central cluster.

4.  Upgrade all secured clusters.

<div>

<div class="title">

Additional resources

</div>

- [Back up the Central database](upgrade-roxctl.md#back-up-central-database_upgrade-roxctl)

- [Upgrade the roxctl CLI](upgrade-roxctl.md#upgrading-roxctl-cli-overview_upgrade-roxctl)

- [Upgrade the Central cluster](upgrade-roxctl.md#upgrading-central-cluster-overview_upgrade-roxctl)

- [Upgrade all secured clusters](upgrade-roxctl.md#upgrading-secured-clusters-overview_upgrade-roxctl)

</div>

<a id="back-up-central-database_upgrade-roxctl"></a>

# Backing up the Central database

You can back up the Central database and use that backup for rolling back from a failed upgrade or data restoration in the case of an infrastructure disaster.

<div>

<div class="title">

Prerequisites

</div>

- You must have an API token with `read` permission for all resources of Red Hat Advanced Cluster Security for Kubernetes. The **Analyst** system role has `read` permissions for all resources.

- You have installed the `roxctl` CLI.

- You have configured the `ROX_API_TOKEN` and the `ROX_CENTRAL_ADDRESS` environment variables.

</div>

<div>

<div class="title">

Procedure

</div>

- Run the backup command:

  ``` terminal
  $ roxctl -e "$ROX_CENTRAL_ADDRESS" central backup
  ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Authenticating by using the roxctl CLI](../cli/using-the-roxctl-cli.md#authenticating-by-using-the-roxctl-cli_using-roxctl-cli)

</div>

<a id="upgrading-roxctl-cli-overview_upgrade-roxctl"></a>

# Upgrading the roxctl CLI

To upgrade the `roxctl` CLI to the latest version you must uninstall the existing version of `roxctl` CLI and then install the latest version of the `roxctl` CLI.

<a id="uninstalling-cli-on-linux_upgrade-roxctl"></a>

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

<a id="installing-cli-on-linux_upgrade-roxctl"></a>

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

<a id="installing-cli-on-macos_upgrade-roxctl"></a>

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

<a id="installing-cli-on-windows_upgrade-roxctl"></a>

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

<a id="upgrading-central-cluster-overview_upgrade-roxctl"></a>

# Upgrading the Central cluster

After you have created a backup of the Central database and generated the necessary resources by using the provisioning bundle, the next step is to upgrade the Central cluster.

This process requires upgrading the `SecurityPolicy` custom resource definition (CRD), Central, and Scanner.

<a id="upgrade-central-cluster-crds_upgrade-roxctl"></a>

## Upgrading the SecurityPolicy custom resource definition

You can update the `SecurityPolicy` custom resource definition (CRD) to the latest version by generating the new CRD and applying it to the cluster.

> [!NOTE]
> If you use Kubernetes, enter `kubectl` instead of `oc`.

<div>

<div class="title">

Procedure

</div>

1.  Use `roxctl` to generate a new set of resources by entering the following command:

    ``` terminal
    $ roxctl central generate k8s pvc > bundle.zip
    ```

2.  Extract the CRD from the archive by entering the following command:

    ``` terminal
    $ unzip bundle.zip central/00-securitypolicy-crd.yaml
    ```

3.  Apply the extracted CRD to your cluster by entering the following command:

    ``` terminal
    $ oc apply -f central/00-securitypolicy-crd.yaml
    ```

</div>

<a id="upgrade-central-cluster-central_upgrade-roxctl"></a>

## Upgrading Central

You can update Central to the latest version by downloading and deploying the updated images.

> [!NOTE]
> If you use Kubernetes, enter `kubectl` instead of `oc`.

<div>

<div class="title">

Procedure

</div>

1.  To update the Central image, run the following command:

    ``` terminal
    $ oc -n stackrox set image deploy/central \
    central=registry.redhat.io/advanced-cluster-security/rhacs-main-rhel9:4.11.3
    ```

2.  To update the Central-db image, run the following command:

    ``` terminal
    $ oc -n stackrox set image deploy/central-db \
    central-db=registry.redhat.io/advanced-cluster-security/rhacs-central-db-rhel9:4.11.3 \
    init-db=registry.redhat.io/advanced-cluster-security/rhacs-central-db-rhel9:4.11.3
    ```

3.  To update the config controller image, run the following command:

    ``` terminal
    $ oc -n stackrox set image deploy/config-controller \
    manager=registry.redhat.io/advanced-cluster-security/rhacs-main-rhel9:4.11.3
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the new pods have deployed:

  ``` terminal
  $ oc get deploy -n stackrox -o wide
  ```

  ``` terminal
  $ oc get pod -n stackrox --watch
  ```

</div>

<a id="upgrade-central-cluster-scanner_upgrade-roxctl"></a>

## Upgrading Scanner

You can update Scanner to the latest version by downloading and deploying the updated images.

> [!IMPORTANT]
> If you are using Kubernetes, enter the `kubectl` command instead of the `oc` command.

<div>

<div class="title">

Procedure

</div>

1.  If you have created custom Scanner configurations, you must apply these changes before updating the Scanner configuration file:

    1.  To generate Scanner, run the following command:

        ``` terminal
        $ roxctl -e "$ROX_CENTRAL_ADDRESS" scanner generate
        ```

    2.  To apply the TLS secrets YAML file, run the following command:

        ``` terminal
        $ oc apply -f scanner-bundle/scanner/02-scanner-03-tls-secret.yaml
        ```

    3.  To apply the Scanner configuration YAML file, run the following command:

        ``` terminal
        $ oc apply -f scanner-bundle/scanner/02-scanner-04-scanner-config.yaml
        ```

2.  To update the Scanner image, run the following command:

    ``` terminal
    $ oc -n stackrox set image deploy/scanner \
    scanner=registry.redhat.io/advanced-cluster-security/rhacs-scanner-rhel9:4.11.3
    ```

3.  To update the Scanner database image, run the following command:

    ``` terminal
    $ oc -n stackrox set image deploy/scanner-db \
    db=registry.redhat.io/advanced-cluster-security/rhacs-scanner-db-rhel9:4.11.3 \
    init-db=registry.redhat.io/advanced-cluster-security/rhacs-scanner-db-rhel9:4.11.3
    ```

</div>

<div>

<div class="title">

Verification

</div>

- To verify that the new pods have been deployed, run the following commands:

  ``` terminal
  $ oc get deploy -n stackrox -o wide
  ```

  ``` terminal
  $ oc get pod -n stackrox --watch
  ```

</div>

<a id="verify-central-cluster-upgrade_upgrade-roxctl"></a>

## Verifying the Central cluster upgrade

After you have upgraded both Central and Scanner, verify that the Central cluster upgrade is complete.

> [!NOTE]
> If you use Kubernetes, enter `kubectl` instead of `oc`.

<div>

<div class="title">

Procedure

</div>

- Check the Central logs by running the following command:

  ``` terminal
  $ oc logs -n stackrox deploy/central -c central
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  No database restore directory found (this is not an error).
  Migrator: 2023/04/19 17:58:54: starting DB compaction
  Migrator: 2023/04/19 17:58:54: Free fraction of 0.0391 (40960/1048576) is < 0.7500. Will not compact
  badger 2023/04/19 17:58:54 INFO: All 1 tables opened in 2ms
  badger 2023/04/19 17:58:55 INFO: Replaying file id: 0 at offset: 846357
  badger 2023/04/19 17:58:55 INFO: Replay took: 50.324µs
  badger 2023/04/19 17:58:55 DEBUG: Value log discard stats empty
  Migrator: 2023/04/19 17:58:55: DB is up to date. Nothing to do here.
  badger 2023/04/19 17:58:55 INFO: Got compaction priority: {level:0 score:1.73 dropPrefix:[]}
  version: 2023/04/19 17:58:55.189866 ensure.go:49: Info: Version found in the DB was current. We’re good to go!
  ```

  </div>

</div>

<a id="upgrading-secured-clusters-overview_upgrade-roxctl"></a>

# Upgrading all secured clusters

After upgrading Central services, you must upgrade all secured clusters. You can use automatic upgrades or manual upgrades depending on your configuration.

If you are using automatic upgrades, follow this guidance:

- Update all your secured clusters by using automatic upgrades.

- For information about troubleshooting problems with the automatic cluster upgrader, see "Troubleshooting the cluster upgrader".

- Skip the instructions in this section and follow the instructions in the "Verify upgrades" and "Revoking the API token" sections.

If you are not using automatic upgrades, you must run the instructions in this section on all secured clusters including the Central cluster.

- To ensure optimal functionality, use the same RHACS version for your secured clusters and the cluster on which Central is installed.

To complete manual upgrades of each secured cluster running Sensor, Collector, and Admission controller, follow the instructions that are provided.

<a id="update-other-images_upgrade-roxctl"></a>

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

<a id="add-pod-namespace-to-sensor-and-admission-control_upgrade-roxctl"></a>

## Adding POD_NAMESPACE to sensor and admission-control deployments

When upgrading to version 4.6 or later from a version earlier than 4.6, you must patch the sensor and admission-control deployments to set the `POD_NAMESPACE` environment variable.

> [!NOTE]
> If you are using Kubernetes, use `kubectl` instead of `oc` for the commands listed in this procedure.

<div>

<div class="title">

Procedure

</div>

1.  Patch sensor to set `POD_NAMESPACE` by running the following command:

    ``` terminal
    $ [[ -z "$(oc -n stackrox get deployment sensor -o yaml | grep POD_NAMESPACE)" ]] && oc -n stackrox patch deployment sensor --type=json -p '[{"op":"add","path":"/spec/template/spec/containers/0/env/-","value":{"name":"POD_NAMESPACE","valueFrom":{"fieldRef":{"fieldPath":"metadata.namespace"}}}}]'
    ```

2.  Patch admission-control to set `POD_NAMESPACE` by running the following command:

    ``` terminal
    $ [[ -z "$(oc -n stackrox get deployment admission-control -o yaml | grep POD_NAMESPACE)" ]] && oc -n stackrox patch deployment admission-control --type=json -p '[{"op":"add","path":"/spec/template/spec/containers/0/env/-","value":{"name":"POD_NAMESPACE","valueFrom":{"fieldRef":{"fieldPath":"metadata.namespace"}}}}]'
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Verifying secured cluster upgrade](upgrade-roxctl.md#verify-secured-cluster-upgrade_upgrade-roxctl)

- [Migrating security context constraints (SCCs) during the manual upgrade](upgrade-roxctl.md#migrating-sccs-during-the-manual-upgrade_upgrade-roxctl)

</div>

<a id="migrating-sccs-during-the-manual-upgrade_upgrade-roxctl"></a>

## Migrating security context constraints during the manual upgrade

By migrating the security context constraints (SCCs) during the manual upgrade by using `roxctl` CLI, you can seamlessly migrate the Red Hat Advanced Cluster Security for Kubernetes (RHACS) services to use the Red Hat OpenShift SCCs, ensuring compatibility and optimal security configurations across Central and all secured clusters.

<div>

<div class="title">

Procedure

</div>

1.  List all RHACS services deployed on Central and all secured clusters:

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

    To add the required roles and role bindings to use the Red Hat OpenShift SCCs for the Central cluster, complete the following steps:

    1.  Create a file named `update-central.yaml` that defines the role and role binding resources by using the following content:

        ``` yaml
        apiVersion: rbac.authorization.k8s.io/v1
        kind: Role #
        metadata:
          annotations:
             email: support@stackrox.com
             owner: stackrox
          labels:
             app.kubernetes.io/component: central
             app.kubernetes.io/instance: stackrox-central-services
             app.kubernetes.io/name: stackrox
             app.kubernetes.io/part-of: stackrox-central-services
             app.kubernetes.io/version: 4.4.0
          name: use-central-db-scc #
          namespace: stackrox #
        Rules: #
        - apiGroups:
          - security.openshift.io
          resourceNames:
          - nonroot-v2
          resources:
          - securitycontextconstraints
          verbs:
          - use
        - - -
        apiVersion: rbac.authorization.k8s.io/v1
        kind: Role
        metadata:
          annotations:
             email: support@stackrox.com
             owner: stackrox
          labels:
             app.kubernetes.io/component: central
             app.kubernetes.io/instance: stackrox-central-services
             app.kubernetes.io/managed-by: Helm
             app.kubernetes.io/name: stackrox
             app.kubernetes.io/part-of: stackrox-central-services
             app.kubernetes.io/version: 4.4.0
          name: use-central-scc
          namespace: stackrox
        rules:
        - apiGroups:
          - security.openshift.io
          resourceNames:
          - nonroot-v2
          resources:
          - securitycontextconstraints
          verbs:
          - use
        - - -
        apiVersion: rbac.authorization.k8s.io/v1
        kind: Role
        metadata:
          annotations:
             email: support@stackrox.com
             owner: stackrox
          labels:
             app.kubernetes.io/component: scanner
             app.kubernetes.io/instance: stackrox-central-services
             app.kubernetes.io/name: stackrox
             app.kubernetes.io/part-of: stackrox-central-services
             app.kubernetes.io/version: 4.4.0
          name: use-scanner-scc
          namespace: stackrox
        rules:
        - apiGroups:
          - security.openshift.io
          resourceNames:
          - nonroot-v2
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
             app.kubernetes.io/component: central
             app.kubernetes.io/instance: stackrox-central-services
             app.kubernetes.io/name: stackrox
             app.k ubernetes.io/part-of: stackrox-central-services
             app.kubernetes.io/version: 4.4.0
          name: central-db-use-scc #
          namespace: stackrox
        roleRef: #
          apiGroup: rbac.authorization.k8s.io
          kind: Role
          name: use-central-db-scc
        subjects: #
        - kind: ServiceAccount
          name: central-db
          namespace: stackrox
        - - -
        apiVersion: rbac.authorization.k8s.io/v1
        kind: RoleBinding
        metadata:
          annotations:
             email: support@stackrox.com
             owner: stackrox
          labels:
             app.kubernetes.io/component: central
             app.kubernetes.io/instance: stackrox-central-services
             app.kubernetes.io/name: stackrox
             app.kubernetes.io/part-of: stackrox-central-services
             app.kubernetes.io/version: 4.4.0
          name: central-use-scc
          namespace: stackrox
        roleRef:
          apiGroup: rbac.authorization.k8s.io
          kind: Role
          name: use-central-scc
        subjects:
        - kind: ServiceAccount
          name: central
          namespace: stackrox
        - - -
        apiVersion: rbac.authorization.k8s.io/v1
        kind: RoleBinding
        metadata:
          annotations:
             email: support@stackrox.com
             owner: stackrox
          labels:
             app.kubernetes.io/component: scanner
             app.kubernetes.io/instance: stackrox-central-services
             app.kubernetes.io/name: stackrox
             app.kubernetes.io/part-of: stackrox-central-services
             app.kubernetes.io/version: 4.4.0
          name: scanner-use-scc
          namespace: stackrox
        roleRef:
          apiGroup: rbac.authorization.k8s.io
          kind: Role
          name: use-scanner-scc
        subjects:
        - kind: ServiceAccount
          name: scanner
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

    2.  Create the role and role binding resources specified in the `update-central.yaml` file by running the following command:

        ``` terminal
        $ oc -n stackrox create -f ./update-central.yaml
        ```

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

    1.  To delete the SCCs that are specific to the Central cluster, run the following command:

        ``` terminal
        $ oc delete scc/stackrox-central scc/stackrox-central-db scc/stackrox-scanner
        ```

    2.  To delete the SCCs that are specific to all secured clusters, run the following command:

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

<a id="verify-secured-cluster-upgrade_upgrade-roxctl"></a>

### Verifying secured cluster upgrade

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

<a id="rhcos-enable-node-scan_upgrade-roxctl"></a>

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

- [Red Hat Advanced Cluster Security for Kubernetes Support Matrix](https://access.redhat.com/articles/7045053)

- [Red Hat Advanced Cluster Security for Kubernetes Support Policy](https://access.redhat.com/support/policy/updates/rhacs)

- [Scanning RHCOS node hosts](../operating/manage-vulnerabilities/scan-rhcos-node-host.md)

</div>

<a id="rollback-central-normal_upgrade-roxctl"></a>

# Rolling back Central normally

You can roll back to a previous version of Central if upgrading Red Hat Advanced Cluster Security for Kubernetes fails.

> [!NOTE]
> If you use Kubernetes, enter `kubectl` instead of `oc`.

<div>

<div class="title">

Prerequisites

</div>

- **Enough disk space**: Before you can perform a rollback, you must have free disk space available on your persistent storage. Red Hat Advanced Cluster Security for Kubernetes uses disk space to keep a copy of databases during the upgrade. If the disk space is not enough to store a copy and the upgrade fails, you cannot perform a roll back to an earlier version.

- **Internal database rollback (4.8 or earlier)**: If you are rolling back from RHACS 4.8 to an earlier version and use the internal database (`central-db`), you must first restore the database from a PostgreSQL 13 backup.

  - To restore the database, add the `RESTORE_BACKUP=true` and `FORCE_OLD_BINARIES=true` environment variables to the `central-db` and `init-db` containers of the `central-db` component.

  - For details on injecting environment variables, see "Injecting an environment variable into the Central deployment".

</div>

<div>

<div class="title">

Procedure

</div>

- Run the following command to roll back to a previous version when an upgrade fails (before the Central service starts):

  ``` terminal
  $ oc -n stackrox rollout undo deploy/central
  ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Injecting an environment variable into the Central deployment](../installing/installing_ocp/install-central-config-options-ocp.md#adding-an-environment-variable-to-a-deployment_install-central-config-options-ocp)

</div>

<a id="rollback-central-forced_upgrade-roxctl"></a>

## Rolling back Central forcefully

You can use forced rollback to roll back to an earlier version of Central (after the Central service starts).

<div class="important">

<div class="title">

</div>

- Using forced rollback to switch back to a previous version might result in loss of data and functionality.

- If you use Kubernetes, enter `kubectl` instead of `oc`.

</div>

<div>

<div class="title">

Prerequisites

</div>

- **Enough disk space**: Before you can perform a rollback, you must have free disk space available on your persistent storage. Red Hat Advanced Cluster Security for Kubernetes uses disk space to keep a copy of databases during the upgrade. If the disk space is not enough to store a copy and the upgrade fails, you cannot perform a roll back to an earlier version.

- **Internal database rollback (4.8 or earlier)**: If you are rolling back from RHACS 4.8 to an earlier version and use the internal database (`central-db`), you must first restore the database from a PostgreSQL 13 backup.

  - To restore the database, add the `RESTORE_BACKUP=true` and `FORCE_OLD_BINARIES=true` environment variables to the `central-db` and `init-db` containers of the `central-db` component.

  - For details on injecting environment variables, see "Injecting an environment variable into the Central deployment".

</div>

<div>

<div class="title">

Procedure

</div>

- Run the following commands to perform a forced rollback:

  - To forcefully rollback to the previously installed version:

    ``` terminal
    $ oc -n stackrox rollout undo deploy/central
    ```

  - To forcefully rollback to a specific version:

    1.  Edit the `ConfigMap` that belongs to Central:

        ``` terminal
        $ oc -n stackrox edit configmap/central-config
        ```

    2.  Update the value of the `maintenance.forceRollbackVersion` key:

        ``` yaml
        data:
          central-config.yaml: |
            maintenance:
              safeMode: false
              compaction:
                 enabled: true
                 bucketFillFraction: .5
                 freeFractionThreshold: 0.75
              forceRollbackVersion: <x.x.x.x>
          ...
        ```

        where:

        `<x.x.x.x>`  
        Specifies the version that you want to roll back to.

    3.  Update the Central image version:

        ``` terminal
        $ oc -n stackrox \
          set image deploy/central central=registry.redhat.io/advanced-cluster-security/rhacs-main-rhel9:<x.x.x.x>
        ```

        where:

        `<x.x.x.x>`  
        Specifies the version that you want to roll back to. It must be the same version that you specified for the `maintenance.forceRollbackVersion` key in the `central-config` config map.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Injecting an environment variable into the Central deployment](../installing/installing_ocp/install-central-config-options-ocp.md#adding-an-environment-variable-to-a-deployment_install-central-config-options-ocp)

</div>

<a id="verify-upgrades_upgrade-roxctl"></a>

# Verifying upgrades

The updated Sensors and Collectors continue to report the latest data from each secured cluster.

The last time Sensor contacted Central is visible in the RHACS portal.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **System Health**.

2.  Check to ensure that Sensor Upgrade shows clusters up to date with Central.

</div>

<a id="revoke-the-api-token_upgrade-roxctl"></a>

# Revoking the API token

For security reasons, Red Hat recommends that you revoke the API token that you have used to complete Central database backup.

<div>

<div class="title">

Prerequisites

</div>

- After the upgrade, you must reload the RHACS portal page and re-accept the certificate to continue using the RHACS portal.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Scroll down to the **Authentication Tokens** category, and click **API Token**.

3.  Select the checkbox in front of the token name that you want to revoke.

4.  Click **Revoke**.

5.  On the confirmation dialog box, click **Confirm**.

</div>

<a id="troubleshooting-upgrader_upgrade-roxctl"></a>

# Troubleshooting the cluster upgrader

If you encounter problems when using the legacy installation method for the secured cluster and enabling the automated updates, you can troubleshoot the problem by examining error messages in the **Platform Configuration** → **Clusters** page. Based on the error type, follow the appropriate troubleshooting procedure.

<a id="troubleshooting-upgrader-missing-permissions_upgrade-roxctl"></a>

## Upgrader missing permissions

If the cluster upgrader is missing permissions, you can resolve this issue by ensuring the bundle was generated correctly or by manually configuring the required service accounts and role bindings.

<div>

<div class="title">

Procedure

</div>

1.  Ensure that the bundle for the secured cluster was generated with future upgrades enabled before clicking **Download YAML file and keys**.

2.  If possible, remove that secured cluster and generate a new bundle making sure that future upgrades are enabled.

3.  If you cannot re-create the cluster, you can take these actions:

    1.  Ensure that the service account `sensor-upgrader` exists in the same namespace as Sensor.

    2.  Ensure that a ClusterRoleBinding exists (default name: `<namespace>:upgrade-sensors`) that grants the `cluster-admin` ClusterRole to the `sensor-upgrader` service account.

</div>

<a id="troubleshooting-upgrader-missing-image_upgrade-roxctl"></a>

## Upgrader cannot start due to missing image

If the upgrader cannot start because it cannot pull the required image, you can resolve this issue by ensuring the secured cluster has access to the registry and the image pull secrets are configured correctly.

<div>

<div class="title">

Procedure

</div>

1.  Ensure that the Secured Cluster can access the registry and pull the image `<image_reference:tag>`.

2.  Ensure that the image pull secrets are configured correctly in the secured cluster.

</div>

<a id="troubleshooting-upgrader-unknown-reason_upgrade-roxctl"></a>

## Upgrader cannot start due to an unknown reason

If the upgrader cannot start and the reason is not immediately clear, you can troubleshoot by checking upgrader permissions and reviewing the logs for more information.

<div>

<div class="title">

Procedure

</div>

1.  Ensure that the upgrader has enough permissions for accessing the cluster objects. For more information, see "Upgrader is missing permissions".

2.  Check the upgrader logs for more insights.

</div>

<a id="getting-upgrader-logs_upgrade-roxctl"></a>

### Getting upgrader logs

If you cannot easily determine the reason that the upgrader failed, you can get the upgrader logs and examine them to try to determine the reason for the failure.

The upgrader deployment is usually only running in the cluster for a short time while doing the upgrades. It is removed later, so accessing its logs using the orchestrator CLI can require proper timing.

<div>

<div class="title">

Procedure

</div>

- Check the upgrader logs for more insights by running the following command:

  ``` terminal
  $ kubectl -n <namespace> logs deploy/sensor-upgrader
  ```

  where:

  `<namespace>`  
  Specifies the namespace in which Sensor is running.

</div>
