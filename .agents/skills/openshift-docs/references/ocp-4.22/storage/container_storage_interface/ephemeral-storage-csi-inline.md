<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can provision temporary, pod-specific storage by using Container Storage Interface (CSI) inline ephemeral volumes that are automatically created at pod deployment and removed at pod termination.

# Overview of CSI inline ephemeral volumes

Traditionally, volumes that are backed by Container Storage Interface (CSI) drivers can only be used with a `PersistentVolume` and `PersistentVolumeClaim` object combination.

CSI inline ephemeral volumes allow you to specify CSI volumes directly in the `Pod` specification, rather than in a `PersistentVolume` object. Inline volumes are ephemeral and do not persist across pod restarts.

CSI inline ephemeral volumes are only available with the following supported CSI drivers:

- Azure File CSI driver

- Secrets Store CSI driver

## Support limitations for CSI inline ephemeral volumes

> [!IMPORTANT]
> The Shared Resource CSI Driver feature is now generally available in Builds for Red Hat OpenShift 1.1. This feature is now removed in OpenShift Container Platform 4.18 and later. To use this feature, ensure that you are using Builds for Red Hat OpenShift 1.1 or later. For information about Builds for Red Hat OpenShift 1.1, see "Builds for Red Hat OpenShift 1.1".

By default, OpenShift Container Platform supports CSI inline ephemeral volumes with these limitations:

- Support is only available for CSI drivers. In-tree and FlexVolumes are not supported.

- Community or storage vendors provide other CSI drivers that support these volumes. Follow the installation instructions provided by the CSI driver provider.

CSI drivers might not have implemented the inline volume functionality, including `Ephemeral` capacity. For details, see the CSI driver documentation.

<div>

<div class="title">

Additional resources

</div>

- [Builds for Red Hat OpenShift 1.1](https://docs.redhat.com/en/documentation/builds_for_red_hat_openshift/1.1)

</div>

# CSI Volume Admission plugin

To restrict Container Storage Interface (CSI) ephemeral volume usage based on pod security standards, the CSI Volume Admission plugin enforces admission policies by inspecting security profile labels on CSI drivers.

## Overview of CSI Volume Admission plugin

The CSI Volume Admission plugin allows you to restrict the use of an individual CSI driver capable of provisioning CSI ephemeral volumes on pod admission. Administrators can add a `csi-ephemeral-volume-profile` label, and this label is then inspected by the Admission plugin and used in enforcement, warning, and audit decisions.

To use the CSI Volume Admission plugin, administrators add the `security.openshift.io/csi-ephemeral-volume-profile` label to a `CSIDriver` object, which declares the CSI driver’s effective pod security profile when it is used to provide CSI ephemeral volumes, as shown in the following example:

<div class="formalpara">

<div class="title">

Example CSIDriver YAML file enabling using of the CSI Admission plugin

</div>

``` yaml
kind: CSIDriver
metadata:
  name: csi.mydriver.company.org
  labels:
    security.openshift.io/csi-ephemeral-volume-profile: restricted
```

</div>

Setting `metadata.labels.security.openshift.io/csi-ephemeral-volume-profile` to `restricted` enables use of the CSI Admission plugin.

This “effective profile” communicates that a pod can use the CSI driver to mount CSI ephemeral volumes when the pod’s namespace is governed by a pod security standard.

The CSI Volume Admission plugin inspects pod volumes when pods are created; existing pods that use CSI volumes are not affected. If a pod uses a container storage interface (CSI) volume, the plugin looks up the `CSIDriver` object and inspects the `csi-ephemeral-volume-profile` label, and then use the label’s value in its enforcement, warning, and audit decisions.

## Pod security profile enforcement

When a CSI driver has the `csi-ephemeral-volume-profile` label, pods using the CSI driver to mount CSI ephemeral volumes must run in a namespace that enforces a pod security standard of equal or greater permission. If the namespace enforces a more restrictive standard, the CSI Volume Admission plugin denies admission. The following table describes the enforcement behavior for different pod security profiles for given label values.

| Pod security profile | Driver label: restricted | Driver label: baseline | Driver label: privileged |
|----|----|----|----|
| Restricted | Allowed | Denied | Denied |
| Baseline | Allowed | Allowed | Denied |
| Privileged | Allowed | Allowed | Allowed |

Pod security profile enforcement

## Pod security profile warning

The CSI Volume Admission plugin can warn you if the CSI driver’s effective profile is more permissive than the pod security warning profile for the pod namespace. The following table shows when a warning occurs for different pod security profiles for given label values.

| Pod security profile | Driver label: restricted | Driver label: baseline | Driver label: privileged |
|----|----|----|----|
| Restricted | No warning | Warning | Warning |
| Baseline | No warning | No warning | Warning |
| Privileged | No warning | No warning | No warning |

Pod security profile warning

## Pod security profile audit

The CSI Volume Admission plugin can apply audit annotations to the pod if the CSI driver’s effective profile is more permissive than the pod security audit profile for the pod namespace. The following table shows the audit annotation applied for different pod security profiles for given label values.

| Pod security profile | Driver label: restricted | Driver label: baseline | Driver label: privileged |
|----|----|----|----|
| Restricted | No audit | Audit | Audit |
| Baseline | No audit | No audit | Audit |
| Privileged | No audit | No audit | No audit |

Pod security profile audit

## Default behavior for the CSI Volume Admission plugin

If the referenced CSI driver for a CSI ephemeral volume does not have the `csi-ephemeral-volume-profile` label, the CSI Volume Admission plugin considers the driver to have the privileged profile for enforcement, warning, and audit behaviors. Likewise, if the pod’s namespace does not have the pod security admission label set, the Admission plugin assumes the restricted profile is allowed for enforcement, warning, and audit decisions. Therefore, if no labels are set, CSI ephemeral volumes using that CSI driver are only usable in privileged namespaces by default.

The CSI drivers that ship with OpenShift Container Platform and support ephemeral volumes have a reasonable default set for the `csi-ephemeral-volume-profile` label:

- Azure File CSI driver: privileged

If desired, an admin can change the default value of the label.

# Embedding a CSI inline ephemeral volume in the pod specification

To provision temporary storage that automatically follows your pod’s lifecycle, embed a Container Storage Interface (CSI) inline ephemeral volume in the pod specification so the CSI driver manages volume creation and cleanup as pods start/stop.

<div>

<div class="title">

Procedure

</div>

1.  Create the `Pod` object definition and save it to a file.

2.  Embed the CSI inline ephemeral volume in the file as in the following pod YAML file:

    <div class="formalpara">

    <div class="title">

    Example pod YAML file with embedded ephemeral volume

    </div>

    ``` yaml
    kind: Pod
    apiVersion: v1
    metadata:
      name: my-csi-app
    spec:
      containers:
        - name: my-frontend
          image: busybox
          volumeMounts:
          - mountPath: "/data"
            name: my-csi-inline-vol
          command: [ "sleep", "1000000" ]
      volumes:
        - name: my-csi-inline-vol
          csi:
            driver: inline.storage.kubernetes.io
            volumeAttributes:
              foo: bar
    ```

    </div>

    Where \`spec.volumes.name\`is the name of the volume that is used by pods.

3.  Create the object definition file that you saved in the previous step by running the following command.

    ``` terminal
    $ oc create -f my-csi-app.yaml
    ```

</div>

# Additional resources

- [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
