<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To support image import and processing, configure the Containerized Data Importer (CDI) scratch space and the required storage class so that CDI can temporarily store and convert virtual machine (VM) images.

# About scratch space

The Containerized Data Importer (CDI) requires scratch space (temporary storage) to complete some operations, such as importing and uploading virtual machine images. During this process, CDI provisions a scratch space PVC equal to the size of the PVC backing the destination data volume (DV).

The scratch space PVC is deleted after the operation completes or aborts.

You can define the storage class that is used to bind the scratch space PVC in the `spec.scratchSpaceStorageClass` field of the `HyperConverged` custom resource.

If the defined storage class does not match a storage class in the cluster, then the default storage class defined for the cluster is used. If there is no default storage class defined in the cluster, the storage class used to provision the original DV or PVC is used.

> [!NOTE]
> CDI requires requesting scratch space with a `file` volume mode, regardless of the PVC backing the origin data volume. If the origin PVC is backed by `block` volume mode, you must define a storage class capable of provisioning `file` volume mode PVCs.

## Manual provisioning

If there are no storage classes, CDI uses any PVCs in the project that match the size requirements for the image. If there are no PVCs that match these requirements, the CDI import pod remains in a **Pending** state until an appropriate PVC is made available or until a timeout function kills the pod.

# CDI operations that require scratch space

To import and process virtual machine (VM) images, the Containerized Data Importer (CDI) uses scratch space as temporary storage during specific operations such as registry imports and image uploads.

| Type | Reason |
|----|----|
| Registry imports | CDI must download the image to a scratch space and extract the layers to find the image file. The image file is then passed to QEMU-IMG for conversion to a raw disk. |
| Upload image | QEMU-IMG does not accept input from STDIN. Instead, the image to upload is saved in scratch space before it can be passed to QEMU-IMG for conversion. |
| HTTP imports of archived images | QEMU-IMG does not know how to handle the archive formats CDI supports. Instead, the image is unarchived and saved into scratch space before it is passed to QEMU-IMG. |
| HTTP imports of authenticated images | QEMU-IMG inadequately handles authentication. Instead, the image is saved to scratch space and authenticated before it is passed to QEMU-IMG. |
| HTTP imports of custom certificates | QEMU-IMG inadequately handles custom certificates of HTTPS endpoints. Instead, CDI downloads the image to scratch space before passing the file to QEMU-IMG. |

# Defining a storage class

You can define the storage class that the Containerized Data Importer (CDI) uses when allocating scratch space by adding the `spec.scratchSpaceStorageClass` field to the `HyperConverged` custom resource (CR).

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `HyperConverged` CR by running the following command:

    ``` terminal
    $ oc edit hyperconverged kubevirt-hyperconverged -n openshift-cnv
    ```

2.  Add the `spec.scratchSpaceStorageClass` field to the CR and set the value to the name of a storage class that exists in the cluster. If you do not specify a storage class, CDI uses the storage class of the persistent volume claim that is being populated.

    ``` yaml
    apiVersion: hco.kubevirt.io/v1beta1
    kind: HyperConverged
    metadata:
      name: kubevirt-hyperconverged
    spec:
      scratchSpaceStorageClass: "<storage_class>"
    ```

3.  Save and exit your default editor to update the `HyperConverged` CR.

</div>

# CDI supported operations matrix

This matrix shows the supported CDI operations for content types against endpoints, and which of these operations requires scratch space.

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Content types</th>
<th style="text-align: left;">HTTP</th>
<th style="text-align: left;">HTTPS</th>
<th style="text-align: left;">Basic HTTP authentication</th>
<th style="text-align: left;">Registry</th>
<th style="text-align: left;">Upload</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>KubeVirt (QCOW2)</p></td>
<td style="text-align: left;"><p>✓ QCOW2</p>
<p>✓ GZ*</p>
<p>✓ XZ*</p></td>
<td style="text-align: left;"><p>✓ QCOW2**</p>
<p>✓ GZ*</p>
<p>✓ XZ*</p></td>
<td style="text-align: left;"><p>✓ QCOW2</p>
<p>✓ GZ*</p>
<p>✓ XZ*</p></td>
<td style="text-align: left;"><p>✓ QCOW2*</p>
<p>□ GZ</p>
<p>□ XZ</p></td>
<td style="text-align: left;"><p>✓ QCOW2*</p>
<p>✓ GZ*</p>
<p>✓ XZ*</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>KubeVirt (raw)</p></td>
<td style="text-align: left;"><p>✓ raw</p>
<p>✓ GZ</p>
<p>✓ XZ</p></td>
<td style="text-align: left;"><p>✓ raw</p>
<p>✓ GZ</p>
<p>✓ XZ</p></td>
<td style="text-align: left;"><p>✓ raw</p>
<p>✓ GZ</p>
<p>✓ XZ</p></td>
<td style="text-align: left;"><p>✓ raw*</p>
<p>□ GZ</p>
<p>□ XZ</p></td>
<td style="text-align: left;"><p>✓ raw*</p>
<p>✓ GZ*</p>
<p>✓ XZ*</p></td>
</tr>
</tbody>
</table>

|      |                                                                      |
|------|----------------------------------------------------------------------|
| ✓    | Supported operation                                                  |
| □    | Unsupported operation                                                |
| \*   | Requires scratch space                                               |
| \*\* | Requires scratch space if a custom certificate authority is required |

# Additional resources

- [Dynamic provisioning](../../storage/dynamic-provisioning.md#about_dynamic-provisioning)
