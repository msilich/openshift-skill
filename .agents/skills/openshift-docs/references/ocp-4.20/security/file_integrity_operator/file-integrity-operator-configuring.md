<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

# Viewing FileIntegrity object attributes

As with any Kubernetes custom resources (CRs), you can run `oc explain fileintegrity`, and then look at the individual attributes using:

``` terminal
$ oc explain fileintegrity.spec
```

``` terminal
$ oc explain fileintegrity.spec.config
```

# Important attributes

| Attribute | Description |
|----|----|
| `spec.nodeSelector` | Specifies a map of key-value pairs that labels for a node must match for a cluster to schedule Advanced Intrusion Detection Environment (AIDE) pods on that node. Typically, you can configure only a single key-value pair. For example, `node-role.kubernetes.io/worker: ""` schedules AIDE on all compute nodes, while `node.openshift.io/os_id: "rhel"` schedules AIDE on all RHEL nodes. |
| `spec.debug` | A boolean attribute. If set to `true`, the daemon running in the AIDE deamon set’s pods would output extra information. |
| `spec.tolerations` | Specify tolerations to schedule on nodes with custom taints. When not specified, a default toleration is applied, which allows tolerations to run on control plane nodes. |
| `spec.config.gracePeriod` | The number of seconds to pause in between AIDE integrity checks. Frequent AIDE checks on a node can be resource intensive, so it can be useful to specify a longer interval. Defaults to `900`, or 15 minutes. |
| `maxBackups` | The maximum number of AIDE database and log backups leftover from the `re-init` process to keep on a node. Older backups beyond this number are automatically pruned by the daemon. |
| `spec.config.name` | Name of a configMap that contains custom AIDE configuration. If omitted, a default configuration is created. |
| `spec.config.namespace` | Namespace of a configMap that contains custom AIDE configuration. If unset, the FIO generates a default configuration suitable for RHCOS systems. |
| `spec.config.key` | Key that contains actual AIDE configuration in a config map specified by `name` and `namespace`. The default value is `aide.conf`. |
| `spec.config.initialDelay` | The number of seconds to wait before starting the first AIDE integrity check. Default is set to 0. This attribute is optional. |

Important `spec` and `spec.config` attributes

# Examine the default configuration

The default File Integrity Operator configuration is stored in a config map with the same name as the `FileIntegrity` CR.

<div>

<div class="title">

Procedure

</div>

- To examine the default config, run:

  ``` terminal
  $ oc describe cm/worker-fileintegrity
  ```

</div>

# Understanding the default File Integrity Operator configuration

Below is an excerpt from the `aide.conf` key of the config map:

``` bash
@@define DBDIR /hostroot/etc/kubernetes
@@define LOGDIR /hostroot/etc/kubernetes
database=file:@@{DBDIR}/aide.db.gz
database_out=file:@@{DBDIR}/aide.db.gz
gzip_dbout=yes
verbose=5
report_url=file:@@{LOGDIR}/aide.log
report_url=stdout
PERMS = p+u+g+acl+selinux+xattrs
CONTENT_EX = sha512+ftype+p+u+g+n+acl+selinux+xattrs

/hostroot/boot/     CONTENT_EX
/hostroot/root/\..* PERMS
/hostroot/root/   CONTENT_EX
```

The default configuration for a `FileIntegrity` instance provides coverage for files under the following directories:

- `/root`

- `/boot`

- `/usr`

- `/etc`

The following directories are not covered:

- `/var`

- `/opt`

- Some OpenShift Container Platform-specific excludes under `/etc/`

# Supplying a custom AIDE configuration

Any entries that configure AIDE internal behavior such as `DBDIR`, `LOGDIR`, `database`, and `database_out` are overwritten by the Operator. The Operator would add a prefix to `/hostroot/` before all paths to be watched for integrity changes. This makes reusing existing AIDE configs that might often not be tailored for a containerized environment and start from the root directory easier.

> [!NOTE]
> `/hostroot` is the directory where the pods running AIDE mount the host’s file system. Changing the configuration triggers a reinitializing of the database.

# Defining a custom File Integrity Operator configuration

This example focuses on defining a custom configuration for a scanner that runs on the control plane nodes based on the default configuration provided for the `worker-fileintegrity` CR. This workflow might be useful if you are planning to deploy a custom software running as a daemon set and storing its data under `/opt/mydaemon` on the control plane nodes.

<div>

<div class="title">

Procedure

</div>

1.  Make a copy of the default configuration.

2.  Edit the default configuration with the files that must be watched or excluded.

3.  Store the edited contents in a new config map.

4.  Point the `FileIntegrity` object to the new config map through the attributes in `spec.config`.

5.  Extract the default configuration:

    ``` terminal
    $ oc extract cm/worker-fileintegrity --keys=aide.conf
    ```

    This creates a file named `aide.conf` that you can edit. To illustrate how the Operator post-processes the paths, this example adds an exclude directory without the prefix:

    ``` terminal
    $ vim aide.conf
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    /hostroot/etc/kubernetes/static-pod-resources
    !/hostroot/etc/kubernetes/aide.*
    !/hostroot/etc/kubernetes/manifests
    !/hostroot/etc/docker/certs.d
    !/hostroot/etc/selinux/targeted
    !/hostroot/etc/openvswitch/conf.db
    ```

    </div>

    Exclude a path specific to control plane nodes:

    ``` terminal
    !/opt/mydaemon/
    ```

    Store the other content in `/etc`:

    ``` terminal
    /hostroot/etc/   CONTENT_EX
    ```

6.  Create a config map based on this file:

    ``` terminal
    $ oc create cm master-aide-conf --from-file=aide.conf
    ```

7.  Define a `FileIntegrity` CR manifest that references the config map:

    ``` yaml
    apiVersion: fileintegrity.openshift.io/v1alpha1
    kind: FileIntegrity
    metadata:
      name: master-fileintegrity
      namespace: openshift-file-integrity
    spec:
      nodeSelector:
          node-role.kubernetes.io/master: ""
      config:
          name: master-aide-conf
          namespace: openshift-file-integrity
    ```

    The Operator processes the provided config map file and stores the result in a config map with the same name as the `FileIntegrity` object:

    ``` terminal
    $ oc describe cm/master-fileintegrity | grep /opt/mydaemon
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    !/hostroot/opt/mydaemon
    ```

    </div>

</div>

# Changing the custom File Integrity configuration

To change the File Integrity configuration, never change the generated config map. Instead, change the config map that is linked to the `FileIntegrity` object through the `spec.name`, `namespace`, and `key` attributes.
